from myGraph import *
import networkx as nx
from communities import *
from calculateNodes import *
import random

# Graph
G,labels,listofNodes,totalInfluence = realGraph("txtfiles/test.txt")
comms,values = commNum(G)
topComms = communityDensity(G,comms)
NoSN = ceil(0.3*G.number_of_nodes())
myInt = G.number_of_nodes()
initial = initialNodesMapping(NoSN,topComms,comms)

# add influence for every edge of the graph
for n in range(0,len(listofNodes)):
    end = list(labels.keys())[list(labels.values()).index(listofNodes[n])]
    totalInfluence[n][0] = checkInfluence(G,end,totalInfluence[n][0])
randomThres(G)
for k in range(0,5):
    counterWhole = 0
    counterComm = 0
    tie = 0
    if(k == 0):
        initialRandom(G)
        label = "Random Threshold"
    elif(k == 1):
        outDegreeThres(G)
        label = "OutDegree Threshold"
    elif(k == 2):
        degreeCentralityThres(G)
        label = "Degree Centrality Threshold"
    elif(k == 3):
        betweenCentralityThres(G)
        label = "Betweenness Centrality  Threshold"
    else:
        mixedThres(G)
        label = "Mixed Centrality  Threshold"
    for k in range(0,1000):
        #print("")
        #print(comms)
        # Whole
        seedNodes = random.sample(set(labels),NoSN)
        #print("Random Seed Nodes for Whole Diffusion")
        #print(seedNodes)
        diffusion = linear_threshold(G,seedNodes,-4)
        #print("Whole Diffusion Outcome")
        #print(diffusion)
        activeNodes,steps = calculateWhole(G, diffusion)
        #print("Total Active Nodes in each step")
        #print(activeNodes)
        wholeList = [(x / myInt)*100 for x in activeNodes]
        
        # Per comm
        totalActive = []
        diffSteps = []
        for e in range(0,len(comms)):
            if(initial[e] > len(comms[e])):
                # assign the right number
                initial[e] = len(comms[e])
            # community
            subGraph = G.subgraph(comms[e])
            randomSeeds = random.sample(set(comms[e]), initial[e])
            #print("Random Seed Nodes for per Comm Diffusion")
            #print(randomSeeds)
            diffusion = linear_threshold(subGraph,randomSeeds,-4)
            #print("Per Comm Diffusion Outcome")
            #print(diffusion)
            # activated nodes per community
            activatedNodes, step = calculateWhole(subGraph,diffusion)
            # sum of total activated nodes
            totalActive = mergeResults(totalActive,activatedNodes)
        perCommList = [(x / myInt)*100 for x in totalActive]
        '''
        for x in range(0,len(perCommList)):
            diffSteps.extend([x])
        # Plots
        # xlabel
        plt.xlabel('Step', size = 30)
        plt.xticks(size = 30)
        # ylabel
        plt.ylabel('Percentage of Active Nodes', size = 30)
        plt.yticks(size = 30)
        # title
        plt.title("Random Seed Nodes", size = 30)
        # x and y label axis range
        #print(wholeList)
        #print(perCommList)
        plt.axis([0, max(len(steps),len(diffSteps)) + 2, 0, 105])
        # plot the line
        plt.plot(steps, wholeList, ls = "-",color = "r", label = "Whole Diffusion",marker = "o")
        plt.plot(diffSteps, perCommList, ls = "--",color = "b", label = "per Community Diffusion",marker = "x")
        # show legend with labels
        legend = plt.legend(loc = 'best', shadow = False)
        frame = legend.get_frame()
        frame.set_facecolor('0.90')
        plt.show()
        '''
        wholeSize = len(wholeList)
        perCommSize = len(perCommList)

        if(wholeList[wholeSize -1] > perCommList[perCommSize -1]):
            counterWhole = counterWhole + 1
        elif(wholeList[wholeSize -1] < perCommList[perCommSize -1]):
            counterComm = counterComm + 1
        else:
            tie = tie + 1
    print(label)        
    print("Whole")     
    print(counterWhole)
    print("Per Comm")
    print(counterComm)
    print("Ties")
    print(tie)
    print()
