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
        #Lower and Upper bounds for random number of nodes
        lower = 3
        upper = 3
        random.seed(datetime.now())

        #Lower <= Upper bound
        if lower <= upper:
                n = randint(lower,upper)
                seed = randint(0,n-1)
        else:
                #Exits programm
                print "ERROR: lower bound must be lower than the upper bound"
                sys.exit()
        #Graph creation
        G = nx.DiGraph()
        labels = {}
        edgeList = {}
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
        return (G,pos,labels,edgeList,seed)


#Drawing of the graph
def graphDraw(G,pos,labels,edgeList):
        #Draw Edges
        nx.draw_networkx_edges(G,pos,edgeList)
        #Graph drawing
        nx.draw_networkx_labels(G,pos,labels)
        plt.show()

def highDegree(G):
        deg = G.degree()
        for e in G.nodes():
                if(deg[e] != 0):
                        i = 1.0 / deg[e]
                        G.node[e]['threshold'] = i
                else:
                        G.node[e]['threshold'] = 1.0
