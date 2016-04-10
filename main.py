# Imports
from linear_threshold import *
from myGraph import *
import networkx as nx
from calculateNodes import *
from communities import *

G,seed,labels,edgeList,nodeList = createGraph()
outcome = linear_threshold(G,[0,1],steps=-4)
print (outcome)
drawstepbystep(G,labels,edgeList,nodeList,outcome)

