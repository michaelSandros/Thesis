#Imports
import community
import matplotlib.pyplot as plt
import networkx as nx
import random
from fileCopy import *
from linear_threshold import *
from datetime import datetime
from communities import *
from random import *
import random
import sys

# random graph creation
def randomGraph(n):
        # lower and upper bounds for random number of nodes
        listofNodes = []
        random.seed(datetime.now())
        # directed graph
        G = nx.DiGraph()
	# empty dictionary of node labels
        labels = {}
        # node insertion
        for e in range(0,n):
                G.add_node(e)
                labels[e] = e
                listofNodes.extend([e])
        # total influence for all nodes
        totalInfluence =  [[0] for x in range(len(listofNodes))]
        # randrom edges
        for n in G.nodes():
                for k in G.nodes():
                        v = randint(0,10)
                        if n != k and v >= 5:
                                G.add_edge(n,k)
                        else:
                                continue 
        return (G,labels,listofNodes,totalInfluence)

# graph from real Twitter data
def realGraph():
    listofNodes = []
    # directed graph
    G = nx.DiGraph()
    # empty dictionary of node labels
    labels = {}
    # open f2 for reading
    f2 = open('txtfiles/newFile.txt', 'r')
    # each line (a node number) of the newFile is extended to a list
    listofEdges = [line.rstrip() for line in open('txtfiles/newFile.txt')]
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
    # add edges
    for y in range(0,len(listofEdges)-1,2):
        # retrieve the label of the node source
        start = list(labels.keys())[list(labels.values()).index(listofEdges[y+1])]
        # retrieve the label of the node destination
        end = list(labels.keys())[list(labels.values()).index(listofEdges[y])]
        G.add_edge(start,end)
    # total influence for all nodes
    totalInfluence =  [[0] for x in range(len(listofNodes))]
    return (G,labels,listofNodes,totalInfluence)

def edges2Nodes():
    # open f1 for reading
    f1 = open('txtfiles/nodesFile.txt', 'r')
    # open f2 for writing
    f2 = open('txtfiles/newFile.txt', 'w')
    # change space with newline
    for line in f1:
        f2.write(line.replace(' ', '\n'))
    f2.close()
    f1.close()

# checks if the new sum is <= 1 and then adds the new influence
def checkInfluence(G,destination,influence):
    nodeSum = 0
    for e in G.edges():
            # get all the edges to the destination
            if (e[1] == destination):
                    # loop
                    while True:
                            i = random.uniform(0,1)/G.in_degree(e[1])
                            # if the new sum is <= 1, then break from the loop
                            # else repeat
                            if(nodeSum + i <= 1):
                                    G[e[0]][e[1]]['influence'] = i
                                    nodeSum = nodeSum + i
                                    break
    return nodeSum
# add activation probabilities     
def addProbs(G):
      for e in G.edges():
           if ('influence' in G[e[0]][e[1]]):
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
        # draw edges
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
                        G.node[e]['threshold'] = i/deg[e]
                        
# random threshold for all nodes in the range [0,1)
def randomThres(G):
        for e in G.nodes():
                G.node[e]['threshold'] = random.uniform(0, 1)

# degree centrality threshold
def degreeCentralityThres(G):
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                G.node[x]['threshold'] = dc[x]
                if(G.node[x]['threshold'] > 1):
                     G.node[x]['threshold'] = 1.0

# betweeness Centrality Threshold                    
def betweenCentralityThres(G):
        bc = nx.betweenness_centrality(G)
        for x  in G.nodes():
                G.node[x]['threshold'] = bc[x]
                if(G.node[x]['threshold'] > 1):
                     G.node[x]['threshold'] = 1.0
                        
# mixed centrality threshold
def mixedThres(G):
        bc = nx.betweenness_centrality(G)
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
             G.node[x]['threshold'] = (1/2*(bc[x] + dc[x]))/max(bc[x],dc[x])
             if(G.node[x]['threshold'] > 1):
                     G.node[x]['threshold'] = 1.0
                             
        
# communities drawing
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
                # all seed nodes are with yellow color
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
    if(len(seeds) == 1):
        print("The following node is the seed of the diffusion:")
    else:
        print("The following nodes are the seeds of the diffusion:")
    for x in range(0,len(seeds)):
        print(labels.get(seeds[x]))

# prints the number of the activated nodes
# in each step
def diffNumbers(outcome,labels):
        for x in range(1,len(outcome)):
                if(len(outcome[x]) > 0):
                        if(len(outcome[x]) == 1):
                                print("The following node is activated in the step %d:" %x)
                        else:
                                print("The following nodes are activated in the step %d:" %x)
                        for i in range(0,len(outcome[x])):
                                print(labels.get(outcome[x][i]))
                else:
                        print("In the step %d no further activations were possible." %x)
                        print("Diffusion terminated")
                        
def diffusionSizes(G,outcome,comms):
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
                nx.set_node_attributes(G, 'counted', False)
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
                                        flag = sameComm(e[0],e[1],comms)
                                        if(flag):
                                                # if the node is not activated
                                                if(G.node[e[1]]['activated'] == False):
                                                        # if the node does not already counted
                                                        if(G.node[e[1]]['counted'] == False):
                                                                # increment counter
                                                                counter = counter + 1
                                                                G.node[e[1]]['counted'] = True
                targetNodes[x + 1] = [counter]
        return activeNodes,targetNodes
