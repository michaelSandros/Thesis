# Imports
from linear_threshold import *
from myGraph import *
import timeit
import networkx as nx
from calculateNodes import *
from communities import *
from plots import *
from fileCopy import*

#fileCopy()
edges2Nodes()
iterations = 20
active1 = [[0] for x in range(0,iterations)]
active2 = [[0] for x in range(0,iterations)]
active3 = [[0] for x in range(0,iterations)]
active4 = [[0] for x in range(0,iterations)]
active5 = [[0] for x in range(0,iterations)]


time1 = [[0] for x in range(0,iterations)]
time2 = [[0] for x in range(0,iterations)]
time3 = [[0] for x in range(0,iterations)]
time4 = [[0] for x in range(0,iterations)]
time5 = [[0] for x in range(0,iterations)]

x = []

G,labels = realGraph()
comms,values = commNum(G)

for i in range(0,iterations):
    print(i)
    G,labels = realGraph()
    totalSum1 = 0
    for e in range(0,len(comms)):
        H  = G.subgraph(comms[e])
        seeds = perComm(H, comms, e)
        outcome = linear_threshold(H, seeds, steps = -4)
        totalperComm = communityCalculation(comms, e, outcome)
        totalSum1 = totalperComm + totalSum1

    outDegreeThres(G)
    totalSum2 = 0
    for e in range(0,len(comms)):
        H  = G.subgraph(comms[e])
        seeds = perComm(H, comms, e)
        outcome = linear_threshold(H, seeds, steps = -4)
        totalperComm = communityCalculation(comms, e, outcome)
        totalSum2 = totalperComm + totalSum2

    degreeCentralityThres(G)
    totalSum3 = 0
    for e in range(0,len(comms)):
        H  = G.subgraph(comms[e])
        seeds = perComm(H, comms, e)
        outcome = linear_threshold(H, seeds, steps = -4)
        totalperComm = communityCalculation(comms, e, outcome)
        totalSum3 = totalperComm + totalSum3
    
    betweenCentralityThres(G)
    totalSum4 = 0
    for e in range(0,len(comms)):
        H  = G.subgraph(comms[e])
        seeds = perComm(H, comms, e)
        outcome = linear_threshold(H, seeds, steps = -4)
        totalperComm = communityCalculation(comms, e, outcome)
        totalSum4 = totalperComm + totalSum4
        
    mixedThres(G)
    totalSum5 = 0
    for e in range(0,len(comms)):
        H  = G.subgraph(comms[e])
        seeds = perComm(H, comms, e)
        outcome = linear_threshold(H, seeds, steps = -4)
        totalperComm = communityCalculation(comms, e, outcome)
        totalSum5 = totalperComm + totalSum5

    active1[i][0] = totalSum1
    active2[i][0] = totalSum2
    active3[i][0] = totalSum3
    active4[i][0] = totalSum4
    active5[i][0] = totalSum5
    x.append([i])
    
print(active1)
print(active2)
print(active3)
print(active4)
print(active5)

activePlot(active1,active2,active3,active4,active5,x)
