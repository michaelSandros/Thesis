#Imports
import community
import matplotlib.pyplot as plt
import networkx as nx
from fileCopy import *
from linear_threshold import *
from independent_cascade import *
from datetime import datetime
from communities import *
from random import *
import random
import sys
import os.path
from plots import *

# random graph creation
def randomGraph(n):
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
                        v = randint(0,9)
                        # if the nodes are not the same
                        # if the random number is bigger than 4
                        # add edge
                        if n != k and v >= 5:
                                G.add_edge(n,k)
                        else:
                                continue 
        return (G,labels,listofNodes,totalInfluence)

# graph from real Twitter data
def realGraph(path):
    listofNodes = []
    # directed graph
    G = nx.DiGraph()
    edges2Nodes(path)
    # empty dictionary of node labels
    labels = {}
    # open f2 for reading
    f2 = open('txtfiles/newFile.txt', 'r')
    # each line (a node number) of the newFile is extended to a list
    listofEdges = [line.rstrip() for line in open('txtfiles/newFile.txt')]
    f2.close()
    # delete the file
    os.remove('txtfiles/newFile.txt')
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

def edges2Nodes(path):
    # open f1 for reading
    f1 = open(path, 'r')
    # open f2 for writing
    f2 = open('txtfiles/newFile.txt', 'w')
    # change space with newline
    for line in f1:
        f2.write(line.replace(' ', '\n'))
    f2.close()
    f1.close()

# check if the new sum is <= 1 and then adds the new influence
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
def addProbs(G,prob):
      for e in G.edges():
           G[e[0]][e[1]]['act_prob'] = prob

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
        deg = G.out_degree()
        for e in G.nodes():
                if(deg[e] != 0):
                        i = G.node[e]['threshold']
                        G.node[e]['threshold'] = 1/deg[e]
                else:
                        G.node[e]['threshold'] = 1
                        
# random threshold for all nodes in the range [0,1)
def randomThres(G):
        for e in G.nodes():
                i = random.uniform(0, 1)
                G.node[e]['threshold'] = i
                G.node[e]['initial_threshold'] = i
                
# return to the initial random thresholds   
def initialRandom(G):
        for e in G.nodes():
                G.node[e]['threshold'] = G.node[e]['initial_threshold']

# degree centrality threshold
def degreeCentralityThres(G):
        dc = nx.degree_centrality(G)
        for x  in G.nodes():
                G.node[x]['threshold'] = dc[x]
                if(G.node[x]['threshold'] > 1):
                     G.node[x]['threshold'] = 1.0

# betweenness Centrality Threshold                    
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
             if(bc[x] == 0 and bc[x] == 0):
                 G.node[x]['threshold'] = 0
             else:
                     G.node[x]['threshold'] = (1/2*(bc[x] + dc[x]))/max(bc[x],dc[x])
                     if(G.node[x]['threshold'] > 1):
                             G.node[x]['threshold'] = 1.0
                             
        
# communities drawing
def commDraw(G,values):
        plt.axis('off')
        nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, with_labels=False)
        plt.show()

# draw the diffusion step by step
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

def wholeBorda(G):
        # total number of nodes
        nodes = G.number_of_nodes()
        # dictionary with degree centrality for each node
        ddc = {}
        # dictionary with closeness centrality for each node
        dcc = {}
        # dictionary with betweenness centrality for each node
        dbc = {}
        ddcList = []
        dccList = []
        dbcList = []
        # dictionaries with votes
        dc = {}
        bc = {}
        cc = {}
        total = {}
        finalList = []
        sorted_total = []
        # list of top nodes
        finalList = []
        # degree centraliy, closeness centrality and betweenness centrality for each node
        degreeC = nx.degree_centrality(G)
        closenessC = nx.closeness_centrality(G)
        betweennessC = nx.betweenness_centrality(G)
        for x in range(0,nodes):
                ddc[x] = degreeC[x]
                dcc[x] = closenessC[x]
                dbc[x] = betweennessC[x]
        # get values
        ddc_values = list(ddc.values())
        dcc_values = list(dcc.values())
        dbc_values = list(dbc.values()) 
        # descending order degree centraliy, closeness centrality and betweenness centrality
        sorted_ddc = sorted(ddc_values, reverse = True)
        sorted_dcc = sorted(dcc_values, reverse = True)
        sorted_dbc = sorted(dbc_values, reverse = True)
        for k in range(0,len(sorted_ddc)):
                # get the key with the the sorted value
                key = list(ddc.keys())[list(ddc.values()).index(sorted_ddc[k])]
                ddcList.extend([key])
                # delete keys to prevent the appereance of the same node multiple times
                # that happens if there are nodes with the same degree centrality
                del ddc[key]
        for k in range(0,len(sorted_dcc)):
                key = list(dcc.keys())[list(dcc.values()).index(sorted_dcc[k])]
                dccList.extend([key])
                # delete keys to prevent the appereance of the same node multiple times
                # that happens if there are nodes with the same closeness centrality
                del dcc[key]
        for k in range(0,len(sorted_dbc)):
                key = list(dbc.keys())[list(dbc.values()).index(sorted_dbc[k])]
                dbcList.extend([key])
                # delete keys to prevent the appereance of the same node multiple times
                # that happens if there are nodes with the same betweenness centrality
                del dbc[key]
        # votes for the top node of each centrality
        votes = nodes - 1
        # votes acording to position of each node
        for k in range(0,len(ddcList)):
                totalVotes = votes - k
                dc[ddcList[k]] = totalVotes
        for k in range(0,len(dbcList)):
                totalVotes = votes - k
                bc[dbcList[k]] = totalVotes
        for k in range(0,len(dccList)):
                totalVotes = votes - k
                cc[dccList[k]] = totalVotes
        for key in dc:
                total[key] = dc[key] + bc[key] + cc[key]
        total_values = list(total.values())
        sorted_total = sorted(total_values, reverse = True)
        # return the nodes according to votes
        for k in range(0,len(sorted_total)):
                key = list(total.keys())[list(total.values()).index(sorted_total[k])]
                finalList.extend([key])
                # delete keys to prevent the appereance of 2 or more same nodes
                del total[key]
        return finalList

def modelDiffusion(G,seedNodes,color,label,diffFlag,marker,ls):
        # linear_threshold or independent cascade
        if(diffFlag == 1):
                diffusion = linear_threshold(G,seedNodes,-4)
                title = "Linear Threshold Model: Top Seed Nodes"
        else:
                diffusion = independent_cascade(G,seedNodes,-4)
                title = "Independent Cascade Model: Top Seed Nodes"
        # sum of activated nodes per step
        activatedNodes, step = calculateWhole(G,diffusion)
        # total number of graph nodes
        myInt = (G.number_of_nodes())
        # percentage of activated nodes to total nodes
        newList = [(x / myInt)*100 for x in activatedNodes]
        print(newList)
        print(title)
        if(diffFlag == 1):
                print(label)
        print(newList)
        print("")
        stepbystepPlot(newList,step,title,label,color,marker,ls)

def wholeDiffusion(G,totalSeeds,topNodes,diffFlag):
        # top totalSeeds nodes according to Borda
        seedNodes = topNodes[0:totalSeeds]
        # linear threshold model
        if(diffFlag == 1):
                # different thresholds
                for k in range(0,5):
                    if(k == 0):
                        initialRandom(G)
                        color = "r"
                        label = "Random Threshold"
                        marker = "o"
                        ls = "-"
                    elif(k == 1):
                        outDegreeThres(G)
                        color = "sienna"
                        label = "OutDegree Threshold"
                        marker = "s"
                        ls = "-."
                    elif(k == 2):
                        degreeCentralityThres(G)
                        color = "m"
                        label = "Degree Centrality Threshold"
                        marker = "x"
                        ls = "--"
                    elif(k == 3):
                        betweenCentralityThres(G)
                        color = "b"
                        label = "Betweenness Centrality  Threshold"
                        marker = "+"
                        ls = ":"
                    else:
                        mixedThres(G)
                        color = "k"
                        label = "Mixed Centrality  Threshold"
                        marker = "."
                        ls = "-"
                    modelDiffusion(G,seedNodes,color,label,diffFlag,marker,ls)
        else:
                ls = "-"
                color = "r"
                label = ""
                marker = "o"
                modelDiffusion(G,seedNodes,color,label,diffFlag,marker,ls)

def randomICdiffusion(G,option7,seeds):
        # label
        if(len(seeds) == 1):
                label = "Seed Node: "
        else:
                label = "Seed Nodes: "
        for x in range(0,len(seeds)):
                label = label + str(seeds[x]) + " "
        # intependent cascade model
        diffusion = independent_cascade(G,seeds,-4)
        title = "Independent Cascade Model: Random Seed Nodes"
        # sum of activated nodes per step
        activatedNodes, steps = calculateWhole(G,diffusion)
        # total number of graph nodes
        myInt = (G.number_of_nodes())
        # percentage of activated nodes to total nodes
        newList = [(x / myInt)*100 for x in activatedNodes]
        print(title)
        print(label)
        print(newList)
        print("")
        # plot for every simulation
        multiplePlots(newList,steps,option7,title,label)

def randomLTdiffusion(G,labels,option,label,randomSeeds,k):
    # label
    title = "Linear Threshold Model Random Seed"
    if(len(randomSeeds) == 1):
                title = title + " Node: "
    else:
                title = title + " Nodes: "
    for x in range(0,len(randomSeeds)):
        title = title + str(randomSeeds[x]) + " "
    # linear threshold model
    diffusion = linear_threshold(G,randomSeeds,-4)
    # sum of activated nodes per step
    activatedNodes, steps = calculateWhole(G,diffusion)
    # total number of graph nodes
    myInt = (G.number_of_nodes())
    # percentage of activated nodes to total nodes
    newList = [(x / myInt)*100 for x in activatedNodes]
    print(title)
    print(label)
    print(newList)
    print("")
    # plot for every simulation
    multiplePlots(newList,steps,k,title,label)

def perCommICDiffusion(G,seedNodes):
    # find communities
    comms, values = commNum(G)
    # steps of the diffusion
    diffSteps = []
    # active 
    totalActive = []
    # top communities accrdoing to density
    topComms = communityDensity(G,comms)
    # seed nodes per community
    initial = initialNodesMapping(seedNodes,topComms,comms)
    # for every community
    for e in range(0,len(comms)):
        # community
        subGraph = G.subgraph(comms[e])
        # top Nodes of the community
        topNodes = commBorda(subGraph,comms,e)
        # if the size of the community is smaller than the number of the seed nodes
        if(initial[e] > len(comms[e])):
                initial[e] = len(comms[e])
        # get the top initial nodes of each community
        commSeeds = topNodes[0:initial[e]]
        # intependent cascade model
        diffusion = independent_cascade(subGraph,commSeeds,-4)
        # title
        title = "Independent Cascade Model: Top Seed Nodes per Community"
        # activated nodes in each step of the community
        activatedNodes, step = calculateWhole(subGraph,diffusion)
        # total active nodes
        totalActive = mergeResults(totalActive,activatedNodes)
    # color
    color = "r"
    # blank label
    label = ""
    # marker
    marker = "o"
    # linestyle
    ls = "-"
    # total nodes of the graph
    myInt = G.number_of_nodes()
    # percentage of activated nodes to total nodes
    newList = [(x / myInt)*100 for x in totalActive]
    # total steps
    for x in range(0,len(newList)):
        diffSteps.extend([x])
    print(title)
    print(newList)
    print("")
    stepbystepPlot(newList,diffSteps,title,label,color,marker,ls)
    plt.show()

def perCommLTDiffusion(G,seedNodes):
    # find communities
    comms, values = commNum(G)
    diffSteps = []
    totalActive = []
    # top communities according to their densities
    topComms = communityDensity(G,comms)
    # initial nodes per community
    initial = initialNodesMapping(seedNodes,topComms,comms)
    title = "Linear Threshold Model: Top Seed Nodes per Community"
    # different thresholds
    for k in range(0,5):
        diffSteps = []
        totalActive = []
        if(k == 0):
            initialRandom(G)
            label = "Random Threshold"
            color = "r"
            marker = "o"
            ls = "-"
        elif(k == 1):
            outDegreeThres(G)
            label = "OutDegree Threshold"
            color = "sienna"
            marker = "s"
            ls = "-."
        elif(k == 2):
            degreeCentralityThres(G)
            label = "Degree Centrality Threshold"
            color = "m"
            marker = "x"
            ls = "--"
        elif(k == 3):
            betweenCentralityThres(G)
            label = "Betweenness Centrality Threshold"
            color = "b"
            marker = "+"
            ls = ":"
        else:
            mixedThres(G)
            label = "Mixed Centrality Threshold"
            color = "k"
            marker = "."
            ls = "-"
        for e in range(0,len(comms)):
                # subgraph
                subGraph = G.subgraph(comms[e])
                # top nodes
                topNodes = commBorda(subGraph,comms,e)
                # if a community has more initial nodes than nodes
                if(initial[e] > len(comms[e])):
                    initial[e] = len(comms[e])
                # top seeds 
                commSeeds = topNodes[0:initial[e]]
                # permorm the IC model
                diffusion = linear_threshold(subGraph,commSeeds,-4)
                # active nodes per step
                activatedNodes, step = calculateWhole(subGraph,diffusion)
                # merge result of the diffusion
                totalActive = mergeResults(totalActive,activatedNodes)
        # total node number
        myInt = (G.number_of_nodes())
        # percentage of activated nodes to total nodes
        newList = [(x / myInt)*100 for x in totalActive]
        print(title)
        print(label)
        print(newList)
        print("")
        # total steps
        for x in range(0,len(newList)):
                diffSteps.extend([x])
        # plot for every simulation
        stepbystepPlot(newList,diffSteps,title,label,color,marker,ls)
    plt.show()
        
def perCommRandomICDiffusion(G,totalSeeds,simulations):
    # total active nodes per step
    totalActive = []
    # communities of the graph
    comms, values = commNum(G)
    # top communities according to the density
    topComms = communityDensity(G,comms)
    # initial nodes per community
    initial = initialNodesMapping(totalSeeds,topComms,comms)
    # plot title
    title = "Independent Cascade Model: Random Seed Nodes per Community"
    # for every simulation
    for i in range(0,simulations):
        # initialize the lists
        diffSteps = []
        totalActive = []
        activatedNodes = []
        # for every community
        for e in range(0,len(comms)):
            # community
            subGraph = G.subgraph(comms[e])
            # if a community has more seed nodes than nodes
            if(initial[e] > len(comms[e])):
                initial[e] = len(comms[e])
            # random seeds 
            randomSeeds = random.sample(set(comms[e]), initial[e])
            # label
            label = "Iteration Number: " + str(i)
            # permorm the IC model
            diffusion = independent_cascade(subGraph,randomSeeds,-4)
            # active nodes per step
            activatedNodes, step = calculateWhole(subGraph,diffusion)
            # merge result of the diffusion
            totalActive = mergeResults(totalActive,activatedNodes)
        # total node number of the graph
        myInt = (G.number_of_nodes())
        # percentage of activated nodes to total nodes
        newList = [(x / myInt)*100 for x in totalActive]
        # total steps
        for x in range(0,len(newList)):
            diffSteps.extend([x])
        print(label)
        print(newList)
        print("")
        # plot for every simulation
        multiplePlots(newList,diffSteps,i,title,label) 
            
def perCommRandomLTDiffusion(G,totalSeeds,simulations):
    # total active nodes per step
    totalActive = []
    # communities of the graph
    comms, values = commNum(G)
    # top communities according to the density
    topComms = communityDensity(G,comms)
    # initial nodes per community
    initial = initialNodesMapping(totalSeeds,topComms,comms)
    # random thresholds
    for i in range(0,simulations):
            sameNodes = []
            title = "Linear Threshold - Random Seed Nodes per Community - Number of Iteration: " + str(i)
            for e in range(0,len(comms)):
                # if a community has more initial nodes than nodes
                if(initial[e] > len(comms[e])):
                    initial[e] = len(comms[e])
                # random seeds 
                randomSeeds = random.sample(set(comms[e]), initial[e])
                sameNodes.append(randomSeeds)
            for k in range(0,5):
                if(k == 0):
                    initialRandom(G)
                    label = " Random Threshold"
                elif(k == 1):
                    outDegreeThres(G)
                    label = "OutDegree Threshold"
                elif(k == 2):
                    degreeCentralityThres(G)
                    label = "Degree Centrality Threshold"
                elif(k == 3):
                    betweenCentralityThres(G)
                    label = "Betweenness Centrality Threshold"
                else:
                    mixedThres(G)
                    label = "Mixed Centrality Threshold "
                # initialize the lists
                diffSteps = []
                totalActive = []
                activatedNodes = []
                # for every community
                for e in range(0,len(comms)):
                    # subgraph
                    subGraph = G.subgraph(comms[e])
                    # permorm the LC model
                    diffusion = linear_threshold(subGraph,sameNodes[e],-4)
                    # active nodes per step
                    activatedNodes, step = calculateWhole(subGraph,diffusion)
                    # merge result of the diffusion
                    totalActive = mergeResults(totalActive,activatedNodes)
                # total node number
                myInt = (G.number_of_nodes())
                # percentage of activated nodes to total nodes
                newList = [(x / myInt)*100 for x in totalActive]
                print(label)
                print(newList)
                print("")
                # total steps
                for x in range(0,len(newList)):
                    diffSteps.extend([x])
                # plot for every simulation
                multiplePlots(newList,diffSteps,k,title,label)
            plt.show()

def IC_CGA(G,totalSeeds,diffFlag):
    # total active nodes per step
    totalActive = []
    diffSteps = []
    # communities of the graph
    comms, values = commNum(G)
    # top communities according to the density
    topComms = communityDensity(G,comms)
    # initial nodes per community
    initial = initialNodesMapping(totalSeeds,topComms,comms)
    for e in range(0,len(comms)):
        # if the length of the community is fewer than the seed nodes assigned to it
        if(initial[e] > len(comms[e])):
            # assign the right number
            initial[e] = len(comms[e])
        # community
        subGraph = G.subgraph(comms[e])
        # perComm CGA: Return the most influential nodes in the community
        seeds = perComm(subGraph,comms,e,G,diffFlag,initial[e])
        # diffusion
        diffusion = independent_cascade(subGraph,seeds,-4)
        # activated nodes per community
        activatedNodes, step = calculateWhole(subGraph,diffusion)
        # sum of total activated nodes
        totalActive = mergeResults(totalActive,activatedNodes)
    title = "Independent Cascade Model: CGA Algorithm"
    color = "r"
    label = ""
    marker = "o"
    ls = "-"
    # total nodes number
    myInt = G.number_of_nodes()
    # percentage of activated nodes to total nodes
    newList = [(x / myInt)*100 for x in totalActive]
    # total steps
    for x in range(0,len(newList)):
        diffSteps.extend([x])
    print(title)
    print(newList)
    print("")
    stepbystepPlot(newList,diffSteps,title,label,color,marker,ls)
    plt.show()
        

def LT_CGA(G,totalSeeds,diffFlag):
    # communities of the graph
    comms, values = commNum(G)
    # top communities according to the density
    topComms = communityDensity(G,comms)
    # initial nodes per community
    initial = initialNodesMapping(totalSeeds,topComms,comms)
    # different thresholds
    for k in range(0,5):
        if(k == 0):
            initialRandom(G)
            label = "Random Threshold"
            color = "r"
            marker = "o"
            ls = "-"
        elif(k == 1):
            outDegreeThres(G)
            label = "OutDegree Threshold"
            color = "b"
            marker = "s"
            ls = "-."
        elif(k == 2):
            degreeCentralityThres(G)
            label = "Degree Centrality Threshold"
            color = "k"
            marker = "x"
            ls = "--"
        elif(k == 3):
            betweenCentralityThres(G)
            label = "Betweenness Centrality"
            color = "m"
            marker = "+"
            ls = ":"
        else:
            mixedThres(G)
            label = "Mixed Centrality Threshold"
            color = "sienna"
            marker = "."
            ls = "-"
        # total active nodes per step
        totalActive = []
        diffSteps = []
        # if the length of the community is fewer than the seed nodes assigned to it
        for e in range(0,len(comms)):
            if(initial[e] > len(comms[e])):
                # assign the right number
                initial[e] = len(comms[e])
            # community
            subGraph = G.subgraph(comms[e])
            # perComm CGA: Return the most influential nodes in the community
            seeds = perComm(subGraph,comms,e,G,diffFlag,initial[e])
            diffusion = linear_threshold(subGraph,seeds,-4)
            # activated nodes per community
            activatedNodes, step = calculateWhole(subGraph,diffusion)
            # sum of total activated nodes
            totalActive = mergeResults(totalActive,activatedNodes)
        # title
        title = "Linear Threshold  Model: CGA Algorithm per Community"
        # total nodes number
        myInt = G.number_of_nodes()
        # percentage of activated nodes to total nodes
        newList = [(x / myInt)*100 for x in totalActive]
        print(title)
        print(label)
        print(newList)
        print("")
        # total steps
        for x in range(0,len(newList)):
            diffSteps.extend([x])
        stepbystepPlot(newList,diffSteps,title,label,color,marker,ls)
    plt.show()
