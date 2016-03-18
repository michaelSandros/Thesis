#Imports
import matplotlib.pyplot as plt
import networkx as nx
import random
from linear_threshold import *
from datetime import datetime
from random import *
import random
import sys

#Lower and Upper bounds for random number of nodes
lower = 3
upper = 4
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
#Node insertion and random threshold for the node
for e in range(n):
        nodeList = G.add_node(e)
        labels[e] = e
        G.node[e]['threshold'] = random.uniform(0, 1)
#Position for all nodes
pos = nx.random_layout(G)
#Draw nodes
nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
#Randrom Edges and random influence
for e in G.nodes():
        for k in G.nodes():
                v = randint(0,10)
                if e != k and v >= 5:
                        i = random.uniform(0, 1)
                        edgeList = G.add_edge(e,k,influence = i)
                else:
                        continue
#Draw Edges
nx.draw_networkx_edges(G,pos,edgeList)
#Call of linear_threshold
p = linear_threshold(G,[2],-4)
print p
#Graph drawing
nx.draw_networkx_labels(G,pos,labels)
plt.show()
