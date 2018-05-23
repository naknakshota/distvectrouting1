# Distance Vector Routing (A Glance at Distributed Algorithms)
Application of distance vector routing using Bellman Ford

To run this program run the programs on separate terminals.
1st parameter is number of routers in the network.
2nd parameter is number of "neighbors" or connected nodes each router has.
3rd and 4th (and 5th/6th, 7th/8th,...etc.) corresond to the port # and the cost of the path to a neighbor router.

For example:

python3 router.py 50001 3 2 50002 2 50003 7
python3 router.py 50002 3 2 50001 2 50003 1
python3 router.py 50003 3 2 50001 7 50002 1



