import networkx as nx
import itertools

# returns the total activated nodes of the diffusion step by step
# in the whole graph
def calculateWhole(G,outcome):
    stepbystep = []
    step = []
    totalSum = 0
    for x in range(0,len(outcome)):
        totalSum = totalSum + len(outcome[x])
        stepbystep.extend([totalSum])
        step.extend([x])
    return stepbystep,step

# returns the total activated nodes of the diffusion in a single community
def communityCalculation(comms,number,outcome):
    # total activated
    counter = 0
    # flag
    flag = False
    # if there is at least 1 seed number in the community with the specific number
    for x in range(0,len(outcome[0])):
        for i in range(0,len(comms[number])):
            if(outcome[0][x] == comms[number][i]):
                flag = True
    # if there is at least 1
    if(flag):
        # find the total activated nodes in that community
        merged = list(itertools.chain.from_iterable(outcome))
        for x in range(0,len(merged)):
            if(merged[x] in comms[number]):
                counter = counter + 1
    return counter

# returns the total activated nodes of the diffusion in the whole graph
def calculateNodes(p,G):
    totalNodes = G.number_of_nodes()
    # all nodes were the seeders of the diffusion
    if(len(p[0]) == totalNodes):
       totalActivated = totalNodes
    # if in the first step noone node is activated
    elif (len(p[1]) == 0):
        totalActivated = len(p[0])
    # else find how many nodes activated
    else:
        totalActivated = len(p[0])
        # for every step find the activated nodes
        # for every sublist
        for e in range  (1,len(p)):
            for k in range (0,len(p[e])):
                totalActivated = totalActivated + 1
    return totalActivated

# add the activated nodes
def mergeResults(totalActive,activatedNodes):
    for e in range(0,len(activatedNodes)):
        if(len(totalActive) == e):
            if e == 0:
                totalActive.extend([0])
            else:
                totalActive.extend([totalActive[e - 1]])
    # for every new community add the activated nodes
    # per step with the previous results
    for e in range(0,len(activatedNodes)):
        totalActive[e] = totalActive[e] + activatedNodes[e]
    e = e + 1
    for k in range(e,len(totalActive)):
        totalActive[k] = activatedNodes[e - 1] + totalActive[k]
    return totalActive
        
        
