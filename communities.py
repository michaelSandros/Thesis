import community
import random
import sys
import operator
from calculateNodes import *
from linear_threshold import *
import networkx as nx

# each community has the label of the nodes they belong
def commNum(G):
    # directed Graph to Undirected
    UG = G.to_undirected()
    # empty lists
    communities = []
    list2 = []
    # find the community that the node belongs
    partition = community.best_partition(UG)
    # get the number of each community
    values = partition.values()
    # max community number
    max_value = max(values)
    part = community.best_partition(UG)
    values = [part.get(node) for node in UG.nodes()]
    # for all communities with numbers from 0 to max_value
    for comm in range (0, max_value+1):
        # for all nodes in the graph 
        for e in UG.nodes():
            # checks if the number of the community
            # is the same with the node's community number
            if(partition[e] == comm):
                # if they match
                # put new node number in the temporary list
                list2.extend([e])
        # put the temporary list to the list
        # communities list will be:
        # [[nodes_of_community0],[nodes_of_community1],....]
        communities.append(list2)
        # delete list content
        list2 = []
    return (communities,values)

# CGA Algorithm
def initialNodes(G,comms):
    # lists for algorithm
    I = []
    newComms = []
    DRmList = []
    tempList = []
    umaxTempList = []
    maxList = []
    M = len(comms)
    # M empty lists
    Ij = [list([]) for _ in range(M)]
    K = 3
    # number of nodes
    N = nx.number_of_nodes(G)
    if N >= K :
        # 2-d (M+1)x(K+1) arrays
        R = [[0 for x in range(K+1)] for x in range(M+1)]
        s = [[0 for x in range(K+1)] for x in range(M+1)]
        # find the K nodes with maximum influence
        for k in range(1,K+1):
            for m in range(1,M+1):
                for l in range(0,len(comms[m-1])):
                    # union I with each node of the community
                    tempList = I + [comms[m-1][l]]
                    # edw mallon prepei na einai ypografima
                    union = linear_threshold(G,tempList,steps = -4)
                    noUnion = linear_threshold(G,I,steps = -4)
                    VaU = communityCalculation(comms,m-1,union)
                    Va = communityCalculation(comms,m-1,noUnion)
                    diff = VaU/N - Va/N
                    DRmList.extend([diff])
                    tempList = []
                # if empty list go to the next community
                if not DRmList:
                    continue
                else:
                    DRm = max(DRmList)
                R[m][k] = max(R[m-1][k],(R[M][k-1]+DRm))
                if (R[m-1][k] >= R[M][k-1] + DRm):
                    s[m][k] = s[m-1][k]
                else:
                    s[m][k] = m
                DRmList = []
            # community numbering begins from 0
            j = s[M][k] - 1
            newComms = []
            newComms.extend(comms[j])
            d = {}
            for l in range(0,len(newComms)):
                umaxTempList = Ij[j] + [newComms[l]]
                jUnion = linear_threshold(G,umaxTempList,steps = -4)
                jnoUnion = linear_threshold(G,Ij[j],steps= -4)
                jVaU = communityCalculation(comms,j,jUnion)
                jVa,steps = calculateNodes(jnoUnion,G)
                jDiff = jVaU/N - jVa/N
                d[newComms[l]] = jDiff
            # returns the max value of the dictionary
            highest = max(d.values())
            # return a list of nodes that have the max value
            maxList = [k for k,v in d.items() if v == highest]
            # get a random node
            umax = random.choice(maxList)
            Ij[j] = Ij[j] + [umax]
            newComms.remove(umax)
            maxList = []
            umaxTempList = []
            I = I + [umax]
            d = {}
        return I
    else:
        print ("ERROR: K must be lower or equal to the number of nodes")
        sys.exit()
            
def perComm(G, comms, e, wholeGraph):
    interComms = []
    interComms.extend(comms[e])
    Ij = []
    d = {}
    K = 3
    NoN = wholeGraph.number_of_nodes()
    N = G.number_of_nodes()
    maxList = []
    # if K >= N then the seeders are all the nodes in the community e
    if K >= N:
        Ij = interComms
    else:
        for i in range(0,K):
            for x in range(0,len(interComms)):
                u = interComms[x]
                temp = Ij + [u]
                union = linear_threshold(G,temp, steps = -4)
                noUnion = linear_threshold(G,Ij,steps = -4)
                unionTotal = communityCalculation(comms,e, union)
                total, steps = calculateNodes(noUnion,wholeGraph)
                d[interComms[x]] = unionTotal/NoN - total/NoN
            # returns the max value of the dictionary
            highest = max(d.values())
            # return a list of nodes that have the max value
            maxList = [k for k,v in d.items() if v == highest]
            # get a random node
            umax = random.choice(maxList)
            Ij = Ij + [umax]
            d = {}
            interComms.remove(umax)
    return Ij
