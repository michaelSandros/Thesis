# Imports
from linear_threshold import *
from myGraph import *
import networkx as nx
from calculateNodes import *
from communities import *

G,labels,edgeList,nodeList = customGraph()
graphDraw(G,labels,edgeList,nodeList)
