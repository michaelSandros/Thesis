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
def randomGraph():
        # lower and Upper bounds for random number of nodes
        lower = 6
        upper = 6
        listofNodes = []
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
        # node insertion and random threshold for the node
        for e in range(0,n):
                G.add_node(e)
                labels[e] = e
                listofNodes.extend([e])
        # total influence for all nodes
        totalInfluence =  [[0] for x in range(len(listofNodes))]
        # randrom Edges and random influence
        for n in G.nodes():
                for k in G.nodes():
                        v = randint(0,10)
                        if n != k and v >= 5:
                                G.add_edge(n,k)
                        else:
                                continue
        
        return (G,labels,listofNodes)

# custom graph creation
def customGraph():
        random.seed(datetime.now())
        listofNodes = []
        # number of nodes
        N = 10
        G = nx.DiGraph()
        labels = {}
        for e in range(0,N):
                G.add_node(e)
                labels[e] = e
                listofNodes.extend([e])
        totalInfluence =  [[0] for x in range(G.number_of_nodes())]
        for x in range(0,N):
                i = random.uniform(0,1)
                if (x == 0):
                        G.add_edge(x,x + 1)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 2)
                if (x == 1):
                        G.add_edge(x,x + 1)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 2)
                if (x == 2):
                        G.add_edge(x,x + 1)
                if (x == 3):
                        G.add_edge(x,x + 1)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 2)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 3)
                if (x == 4):
                        G.add_edge(x,x + 1)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 2)
                if (x == 5):
                        G.add_edge(x,x + 1)
                if (x == 6):
                        G.add_edge(x,x + 1)
                        i = random.uniform(0,1)
                        edgeList = G.add_edge(x,x + 2)
                        i = random.uniform(0,1)
                        G.add_edge(x,x + 3)
                if (x == 7):
                        G.add_edge(x,x + 2)
                if(x == 8):
                        G.add_edge(x,x + 1)
        return (G,labels,listofNodes)

# graph from real Twitter data
def realGraph():
        
    listofNodes = []
    G = nx.DiGraph()
    labels = {}

    # open f2 for reading
    f2 = open('newFile.txt', 'r')
    # each line (a node number) of the newFile is extended to a list
    listofEdges = [line.rstrip() for line in open('newFile.txt')]
    f2.close()

    # list of chars -> list of integers
    listofEdges = list(map(int, listofEdges))

    # get distinct number of nodes
    for i in listofEdges:
      if i not in listofNodes:
        listofNodes.append(i)
        
    # insert nodes with labels
    for x in range(0,len(listofNodes)):
        G.add_node(x)
        labels[x] = listofNodes[x]
        
    for y in range(0,len(listofEdges)-1,2):
        # retrieve the label of the node source
        start = list(labels.keys())[list(labels.values()).index(listofEdges[y+1])]
        # retrieve the label of the node destination
        end = list(labels.keys())[list(labels.values()).index(listofEdges[y])]
        G.add_edge(start,end)

    # total influence for all nodes
    totalInfluence =  [[0] for x in range(len(listofNodes))]

    return G,labels,listofNodes

def edges2Nodes():
    
    f1 = open('nodesFile.txt', 'r')
    f2 = open('newFile.txt', 'w')
    # change space with newline
    for line in f1:
        f2.write(line.replace(' ', '\n'))
    f2.close()
    f1.close()



def checkInfluence(G,destination,influence):
    nodeSum = 0
    for e in G.edges():
            if (e[1] == destination):
                    while True:
                            i = random.uniform(0,1)/G.in_degree(e[1])
                            if(nodeSum + i <= 1):
                                    G[e[0]][e[1]]['influence'] = i
                                    nodeSum = nodeSum + i
                                    break
    return nodeSum
    
def addProbs(G):
      for e in G.edges():
           del(G[e[0]][e[1]]['influence'])
           random.seed(datetime.now())
           i = random.uniform(0,1)
           G[e[0]][e[1]]['act_prob'] = i

# drawing of the graph
def graphDraw(G,labels):
        # position for all nodes
        pos = nx.random_layout(G)
        # draw nodes
        nx.draw_networkx_nodes(G,pos)
        # draw Edges
        nx.draw_networkx_edges(G,pos)
        # graph drawing
        nx.draw_networkx_labels(G,pos,labels)
        # axis off
        plt.axis('off')
        plt.show()

# the threshold for i-th node is threshold/deg(i)
# if the node has out_degree = 0 then the threshold remains the same(random)
def outDegreeThres(G):
	# out degree for each node
        deg = G.out_degree()
        for e in G.nodes():
                if(deg[e] != 0):
                        i = G.node[e]['threshold']
                        G.node[e]['threshold'] = i
                        
# random threshold for all nodes in the range [0,1)
def randomThres(G):
        for e in G.nodes():
                G.node[e]['threshold'] = random.uniform(0, 1)

# degree centrality threshold
def degreeCentralityThres(G):
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                if(dc[x] != 0):
                        G.node[x]['threshold'] = dc[x]
                        if(G.node[x]['threshold'] > 1):
                             G.node[x]['threshold'] = 1.0

# betweeness Centrality Threshold                    
def betweenCentralityThres(G):
        bc = nx.betweenness_centrality(G)
        for x  in G.nodes():
                if(bc[x] != 0):
                        G.node[x]['threshold'] = bc[x]
                        if(G.node[x]['threshold'] > 1):
                             G.node[x]['threshold'] = 1.0
                        
# mixed Centrality Threshold
def mixedThres(G):
        bc = nx.betweenness_centrality(G)
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                if(bc[x] != 0 or dc[x] != 0):
                     G.node[x]['threshold'] = (1/2*(bc[x] + dc[x]))/max(bc[x],dc[x])
                     if(G.node[x]['threshold'] > 1):
                             G.node[x]['threshold'] = 1.0
                             
        
# communities Drawing
def commDraw(G,values):
        plt.axis('off')
        nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, with_labels=False)
        plt.show()

# draws the diffusion step by step
def drawstepbystep(G,outcome,labels):
        # positions for all nodes
        pos=nx.spring_layout(G)
        activeList = []
        for e in range(1,len(outcome)):
                # all inactive are with red colors
                nx.draw_networkx_nodes(G,pos)
                # all seed nodes are with green color
                nx.draw_networkx_nodes(G,pos,nodelist=outcome[0],node_color='yellow')
                # nodes to be activated in the next step with blue colors
                nx.draw_networkx_nodes(G,pos,nodelist=outcome[e],node_color='blue')
                # activated nodes with green color
                nx.draw_networkx_nodes(G,pos,nodelist=activeList,node_color='green')
		# extend the list with newly activated nodes
                activeList.extend(outcome[e])
                # draw Edges
                nx.draw_networkx_edges(G,pos)
                # draph drawing
                nx.draw_networkx_labels(G,pos,labels)
                # axis off
                plt.axis('off')
                plt.show()
        
# prints the nodes in every community
def label2number(comms,labels):
    for x in range(0,len(comms)):
        if (len(comms[x]) > 1):
            print("The following nodes belong in the Community %d:" %x)
        else:
            print("The following node belongs in the Community %d:" %x)
        for i in range(0,len(comms[x])):
            print(labels.get(comms[x][i]))

# prints the number of the seed nodes
def seedNum(seeds,labels):
    for x in range(0,len(seeds)):
        print(labels.get(seeds[x]))

# prints the number of the activated nodes
# in each step
def diffNumbers(outcome,labels):
        for x in range(1,len(outcome)):
                if(len(outcome[x]) > 0):
                        print("Nodes activated in the step %d" %x)
                        for i in range(0,len(outcome[x])):
                                print(labels.get(outcome[x][i]))
                        print()
                else:
                        print("All other nodes stayed inactive")
def Sizes(G,outcome):
        # set activated flag for all nodes to False
        nx.set_node_attributes(G, 'activated', False)
        counter = 0
        targetCounter = 0
        # list of activated nodes
        activatedList = []
        targetNodes = [[0] for x in range(0,len(outcome))]
        activeNodes = [[0] for x in range(0,len(outcome))]
        
        active = [[0] for x in range(0,len(outcome))]
        # find the activated set of nodes in each step of the diffusion
        for x in range(0,len(outcome) - 1):
                for e in range(0,len(outcome[x])):
                       counter = counter + 1;
                activeNodes[x + 1] = [counter]
                
        # find the target set of nodes in each step of the diffusion        
        for x in range(0,len(outcome) - 1):
                counter = 0
                # extend the list with the new activated nodes
                activatedList.extend(outcome[x])
                # set the activated flag of the nodes to True when the node is active
                for n in range(0,len(activatedList)):
                        G.node[activatedList[n]]['activated'] = True
                        
                # for all elements in the list
                for i in range(0,len(activatedList)):
                        # for all edges
                        for e in G.edges():
                                # if the edge source is the same with the i-th element of the list
                                if (e[0] == activatedList[i]):
                                        # if the node is not activated
                                        if(G.node[e[1]]['activated'] == False):
                                                #increment counter
                                                counter = counter + 1
                targetNodes[x + 1] = [counter]
        return activeNodes,targetNodes
