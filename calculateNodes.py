import networkx as nx

# returns the total activated nodes of the diffusion and the steps
# in the whole graph
def calculateNodes(G,outcome):
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
