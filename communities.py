import community
import random
import sys
from calculateNodes import *
from linear_threshold import *
import networkx as nx

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
    DRmList = []
    tempList = []
    umaxTempList = []
    maxList = []
    M = len(comms)
    Ij = [list([]) for _ in range(M)]
    K = 1
    # number of nodes
    N = nx.number_of_nodes(G)
    if N >= K :
        # 2-d (M+1)x(K+1) arrays
        R = [[0 for x in range(K+1)] for x in range(M+1)]
        s = [[0 for x in range(K+1)] for x in range(M+1)]
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
            # for the j-th community
            for l in range(0,len(comms[j])):
                umaxTempList = Ij[j] + [comms[j][l]]
                jUnion = linear_threshold(G,umaxTempList,steps = -4)
                jnoUnion = linear_threshold(G,Ij[j],steps= -4)
                jVaU = communityCalculation(comms,j,jUnion)
                jVa = calculateNodes(jnoUnion,G)
                jDiff = jVaU/N - jVa/N
                maxList.extend([jDiff])
            # max value of the list
            m = max(maxList)
            # index(-es) of the max value
            maxIndex = [i for i, j in enumerate(maxList) if j == m]
            # if there are more than one index with max value
            # get a random index
            randommaxIndex = random.choice(maxIndex)
            # get the node with that index
            umax = comms[j][randommaxIndex]
            # extend the lists with the node
            I.extend([umax])
            Ij[j].extend([umax])
            # delete the node of the j-th community 
            comms[j].remove(umax)
            maxList = []
        # retun the seeders
        return I
    else:
        print ("ERROR: K must be lower or equal to the number of nodes")
        sys.exit()

