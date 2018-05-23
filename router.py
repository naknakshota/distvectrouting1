#*******************************************************************
#                     Distance Vector Routing
#                      Author: Shota Nakamura
# Objective: Implement distance vector routing using Bellman Ford
#            
#*******************************************************************
from socket import *
import struct
import sys
import time
import _pickle as pickle
import math

class VectorRouting:

    def __init__(self, PORT,NUM_ROUTERS,NUM_NBRS,d):
        self.PORT = PORT
        self.NUM_ROUTERS = NUM_ROUTERS
        self.NUM_NBRS = NUM_NBRS
        self.dict = d


    def calculateVector(self):
        routerSock = socket(AF_INET, SOCK_DGRAM)
        routerSock.bind(('',self.PORT))

        while True:
            #We want to send updates every second
            print(self.dict)
            time.sleep(1)

            #Encode dictionry
            encodeMsg = pickle.dumps(self.dict,-1)
            
            #Send dictionary to all ports in dictionary (This happens every second)
            for key, value in self.dict.items():
                try:
                    routerSock.sendto(encodeMsg,('',key))
                    #routerSock.sendto(encodeMsg,(str(self.PORT),key))
                except:
                    print("Nonexistent Router")
            try:    
                #Receive a message (recvfrom is for unconnected)
                msg,address = routerSock.recvfrom(1024) #Must be recvfrom since this is unconnected
                #decode the message
                decodemsg = pickle.loads(msg)
                addr = address[1]

                for key in decodemsg:
                    if(key not in self.dict):
                        self.dict[key] = math.inf #sets nonexistent edge to infinity

                self.dict = self.bellmanFord(self.dict,decodemsg,addr)


            except:
                continue

    def bellmanFord(self,dict1,dict2,addr):
    #Runs a shortest path algorithm (Bellman-Ford)
        for keys in dict2:
            if(dict1[keys] > dict1[addr] + dict2[keys]):
                dict1[keys] = dict1[addr] + dict2[keys]
            else:
                continue

        return dict1


def main():

    print (sys.argv, len(sys.argv))
    #Number on which this particular router listens
    PORT = int(sys.argv[1])
    #Total number of routers in network
    NUM_ROUTERS = int(sys.argv[2])
    #Number of neighbors
    NUM_NBRS = int(sys.argv[3]) 
    #Create dictionary
    d = {}
    #Instantiate PORT cost as 0
    d[PORT] = 0

    for i in range(0,NUM_NBRS+1,2):
        nbr = int(sys.argv[4+i])
        d[int(nbr)] = int(sys.argv[4+(i+1)])

    #Instead of feeding NBR1 COST1, we feed in the entire dictionary that is already created
    router = VectorRouting(PORT, NUM_ROUTERS, NUM_NBRS,d)
    router.calculateVector()

if __name__ == '__main__':
    main()

