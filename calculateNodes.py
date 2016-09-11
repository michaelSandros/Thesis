import networkx as nx

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

# returns the total activated nodes of the diffusion
# in a single community
def communityCalculation(comms,number,outcome):
    totalActivated = 0
    # converts the list of lists to a single list
    flattend = [val for sublist in outcome for val in sublist]
    # calculates the seed nodes of the communiy to the totalActivated nodes sum
    for x in range(0,len(comms[number])):
        for e in range(0,len(outcome[0])):
            if(comms[number][x] == outcome[0][e]):
                totalActivated = totalActivated + 1
    # removes the seed nodes from the list
    for x in range(0,len(outcome[0])):
        k = outcome[0][x]
        flattend.remove(k)
    # the counter increments when a node in the community
    # is activated by the diffusion
    for i in range(0,len(comms[number])):
        for x in range(0,len(flattend)):
            if(comms[number][i] == flattend[x]):
                totalActivated = totalActivated + 1
    return totalActivated

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

def mergeResults(totalActive,activatedNodes):
    for e in range(0,len(activatedNodes)):
        if(len(totalActive) == e):
            if e == 0:
                totalActive.extend([0])
            else:
                totalActive.extend([totalActive[e - 1]])
    for e in range(0,len(activatedNodes)):
        totalActive[e] = totalActive[e] + activatedNodes[e]
    e = e + 1
    for k in range(e,len(totalActive)):
        totalActive[k] = activatedNodes[e - 1] + totalActive[k]
    return totalActive
        
        
