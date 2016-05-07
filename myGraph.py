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

# random graph creation
def createGraph():
        # lower and Upper bounds for random number of nodes
        lower = 10
        upper = 10
        random.seed(datetime.now())
        # lower <= Upper bound
        if lower <= upper:
                n = randint(lower,upper)
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
        randomThres(G)

        # randrom Edges and random influence
        for e in G.nodes():
                for k in G.nodes():
                        v = randint(0,10)
                        if e != k and v >= 5:
                                i = random.uniform(0, 1)
                                edgeList = G.add_edge(e,k,influence = i)
                        else:
                                continue
        return (G,labels,edgeList,nodeList)

# custom graph creation
def customGraph():
        # number of nodes
        N = 10
        G = nx.DiGraph()
        labels = {}
        edgeList = {}
        for e in range(0,N):
                nodeList = G.add_node(e)
                labels[e] = e
        randomThres(G)
        for x in range(0,N):
                i = random.uniform(0,1)
                if (x == 0):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2,influence = i)
                if (x == 1):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2,influence = i)
                if (x == 2):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                if (x == 3):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 3,influence = i)
                if (x == 4):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2,influence = i)
                if (x == 5):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                if (x == 6):
                        edgeList = G.add_edge(x,x + 1,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2,influence = i)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 3,influence = i)
                if (x == 7):
                        edgeList = G.add_edge(x,x + 2,influence = i)
                if(x == 8):
                        edgeList = G.add_edge(x,x + 1,influence = i)
        return (G,labels,edgeList,nodeList)
        
# drawing of the graph
def graphDraw(G,labels,edgeList,nodeList):
        # position for all nodes
        pos = nx.random_layout(G,scale = 10.0)
        # draw nodes
        nx.draw_networkx_nodes(G,pos,nodelist=nodeList)
        # draw Edges
        nx.draw_networkx_edges(G,pos,edgeList)
        # graph drawing
        nx.draw_networkx_labels(G,pos,labels)
        # axis off
        plt.axis('off')
        plt.show()

# the threshold for i-th node is threshold/deg(i)
# if the node has out_degree = 0 then the threshold remains the same
def outDegreeThres(G):
	# out degree for each node
        deg = G.out_degree()
        for e in G.nodes():
                if(deg[e] != 0):
                        i = G.node[e]['threshold'] / deg[e]
                        G.node[e]['threshold'] = i
                        
# random threshold for all nodes in the range [0,1)
def randomThres(G):
        for e in G.nodes():
                G.node[e]['threshold'] = random.uniform(0, 1)

# the threshold for i-th node is threshold/degree_centrality(i)
# if the node has degree_centrality = 0 then the threshold remains the same(random)
def degreeCentralityThres(G):
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                if(dc[x] != 0):
                        G.node[x]['threshold'] = dc[x]
                        
# the threshold for i-th node is threshold/degree_centrality(i)
# if the node has degree_centrality = 0 then the threshold remains the same(random)
def betweenCentralityThres(G):
        bc = nx.betweenness_centrality(G)
        for x  in G.nodes():
                if(bc[x] != 0):
                        G.node[x]['threshold'] = bc[x]

def mixedThres(G):
        bc = nx.betweenness_centrality(G)
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                if(bc[x] != 0 or dc[x] != 0):
                     G.node[x]['threshold'] = 1/2*(bc[x] + dc[x])    
        

# communities Drawing
def commDraw(G,values):
        nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, with_labels=True)
        plt.show()


def drawstepbystep(G,labels,edgeList,nodeList,outcome):
        # positions for all nodes
        pos=nx.spring_layout(G)
        activeList = []
        for e in range(1,len(outcome)):
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
