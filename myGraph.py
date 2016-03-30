#Imports
import matplotlib.pyplot as plt
import networkx as nx
import random
from linear_threshold import *
from datetime import datetime
from random import *
import random
import sys

def createGraph():
        # lower and Upper bounds for random number of nodes
        lower = 5
        upper = 5
        random.seed(datetime.now())

        # lower <= Upper bound
        if lower <= upper:
                n = randint(lower,upper)
                seed = randint(0,n-1)
        else:
                # exits programm
                print ("ERROR: lower bound must be lower than the upper bound")
                sys.exit()
        # graph creation
        G = nx.DiGraph()
        labels = {}
        edgeList = {}
        # node insertion and random threshold for the node
        for e in range(n):
                nodeList = G.add_node(e)
                labels[e] = e
                G.node[e]['threshold'] = random.uniform(0, 1)
        # position for all nodes
        pos = nx.random_layout(G)
        # draw nodes
        nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
        # randrom Edges and random influence
        for e in G.nodes():
                for k in G.nodes():
                        v = randint(0,10)
                        if e != k and v >= 5:
                                i = random.uniform(0, 1)
                                edgeList = G.add_edge(e,k,influence = i)
                        else:
                                continue
        return (G,pos,labels,edgeList,seed)


# drawing of the graph
def graphDraw(G,pos,labels,edgeList):
        # Draw Edges
        nx.draw_networkx_edges(G,pos,edgeList)
        # Graph drawing
        nx.draw_networkx_labels(G,pos,labels)
        plt.show()

def highDegree(G):
		# out degree for each node
        deg = G.out_degree()
		# the threshold for the nodes is 1/deg
        for e in G.nodes():
                if(deg[e] != 0):
                        i = 1.0 / deg[e]
                        G.node[e]['threshold'] = i
                else:
                        G.node[e]['threshold'] = 1.0
