import networkx as nx

# returns the total activated nodes of the diffusion
def calculateNodes(p,G):
    totalActivated = 0
    totalNodes = len(G)
    steps = len(p) - 1
    # all nodes were the seeders of the diffusion
    if(len(p[0]) == totalNodes):
       totalActivated = totalNodes
    # if in the first step noone node is activated
    elif (len(p[1]) == 0):
        totalActivated = 0
    # else find how many nodes activated
    else:
        # for every step find the activated nodes
        for e in range  (1,len(p)):
            for k in range (0,len(p[e])):
                totalActivated = totalActivated + 1
    return totalActivated,steps

def communityCalculation(comms,number,outcome):
    totalActivated = 0
    # converts the list of list to a single list
    flattend = [val for sublist in outcome for val in sublist]
    # removes the seed nodes from the list
    for x in range(0,len(outcome[0])):
        k = outcome[0][x]
        flattend.remove(k)
    for i in range(0,len(comms[number])):
        for x in range(0,len(flattend)):
            if(comms[number][i] == flattend[x]):
                totalActivated = totalActivated + 1

    return totalActivated
        
            
