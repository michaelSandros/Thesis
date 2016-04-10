#Imports
import community
import matplotlib.pyplot as plt
import networkx as nx
import random
from linear_threshold import *
from datetime import datetime
from random import *
import random
import sys

# graph creation
def createGraph():
        # lower and Upper bounds for random number of nodes
        lower = 10
        upper = 10
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

        # randrom Edges and random influence
        for e in G.nodes():
                for k in G.nodes():
                        v = randint(0,10)
                        if e != k and v >= 5:
                                i = random.uniform(0, 1)
                                edgeList = G.add_edge(e,k,influence = i)
                        else:
                                continue
        return (G,seed,labels,edgeList,nodeList)


# drawing of the graph
def graphDraw(G,labels,edgeList,nodeList):
        # position for all nodes
        pos = nx.spring_layout(G)
        # draw nodes
        nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
        # draw Edges
        nx.draw_networkx_edges(G,pos,edgeList)
        # graph drawing
        nx.draw_networkx_labels(G,pos,labels)
        # axis off
        plt.axis('off')
        plt.show()

def outDegree(G):
	# out degree for each node
        deg = G.out_degree()
	# the threshold for the nodes is 1/deg
        for e in G.nodes():
                if(deg[e] != 0):
                        i = 1.0 / deg[e]
                        G.node[e]['threshold'] = i
                else:
                        G.node[e]['threshold'] = 1.0
# communities Drawing
def commDraw(G,values):
        nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=5000, with_labels=True)
        plt.show()


def drawstepbystep(G,labels,edgeList,nodeList,outcome):
        # positions for all nodes
        pos=nx.spring_layout(G)
        activeList = []
        for e in range(1,len(outcome)):
                print(outcome[e])
                # all inactive are with red colors
                nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
                # all seed nodes are with cyan color
                nx.draw_networkx_nodes(G,pos,nodelist=outcome[0],node_color='green')
                # nodes to be activated in the next step with blue colors
                nx.draw_networkx_nodes(G,pos,nodelist=outcome[e],node_color='blue')
                # activated nodes with green color
                nx.draw_networkx_nodes(G,pos,nodelist=activeList,node_color='green')
				# extend the list with newly activated nodes
                activeList.extend(outcome[e])
                # draw Edges
                nx.draw_networkx_edges(G,pos,edgeList)
                # draph drawing
                nx.draw_networkx_labels(G,pos,labels)
                # axis off
                plt.axis('off')
                plt.show()
