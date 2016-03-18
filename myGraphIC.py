#Imports
import matplotlib.pyplot as plt
import networkx as nx
import random
from independent_cascade import *
from datetime import datetime
from random import *
import random
import sys

#Lower and Upper bounds for random number of nodes
lower = 3
upper = 5
random.seed(datetime.now())

#Lower <= Upper bound
if lower <= upper:
        n = randint(lower,upper)
else:
	#Exits programm
        print "ERROR: lower bound must be lower than the upper bound"
        sys.exit()
#Graph creation
G = nx.DiGraph()
labels = {}
#Node insertion and random activation probality for the node
for e in range(n):
        nodeList = G.add_node(e)
        labels[e]=e
        G.node[e]['prob'] = random.uniform(0, 1)
#Position for all nodes
pos = nx.random_layout(G)
#Draw nodes
nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
#Randrom Edges and random activation probality
for e in G.nodes():
        for k in G.nodes():
                v = randint(0,10)
                if e != k and v >= 5:
                        ap = random.uniform(0, 1)
                        edgeList = G.add_edge(e,k,influence = ap)
                else:
                        continue
#Draw Edges
nx.draw_networkx_edges(G,pos,edgeList)
#Call of linear_threshold
p = independent_cascade(G,[2],100000000000000000)
print p
#Graph drawing
nx.draw_networkx_labels(G,pos,labels)
plt.show()
