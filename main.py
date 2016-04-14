# Imports
from linear_threshold import *
from myGraph import *
import networkx as nx
from calculateNodes import *
from communities import *

G,seed,labels,edgeList,nodeList = createGraph()
comms,values = commNum(G)
seeds = initialNodes(G,comms)
print ("The seeds are")
print(seeds)
