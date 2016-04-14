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
    I = []
    DRmList = []
    tempList = []
    umaxTempList = []
    maxList = []
    M = len(comms)
    Ij = [list([]) for _ in range(M)]
    K = 3
    # number of nodes
    N = nx.number_of_nodes(G)
    if N >= K :
        # 2-d (M+1)x(K+1) arrays
        R = [[0 for x in range(K+1)] for x in range(M+1)]
        s = [[0 for x in range(K+1)] for x in range(M+1)]
        print(comms)
        for k in range(1,K+1):
            for m in range(1,M+1):
                for l in range(0,len(comms[m-1])):
                    #union
                    tempList = I + [comms[m-1][l]]
                    # edw mallon prepei na einai ypografima
                    union = linear_threshold(G,tempList,steps = -4)
                    noUnion = linear_threshold(G,I,steps = -4)
                    VaU = calculateNodes(union,G)
                    Va = calculateNodes(noUnion,G)
                    diff = VaU/N - Va/N
                    DRmList.extend([diff])
                    tempList = []
                if not DRmList:
                    continue
                else:
                    DRm = max(DRmList)
                R[m][k] = max(R[m-1][k],R[M][k-1]+DRm)
                if (R[m-1][k] >= R[M][k-1] + DRm):
                    print("Hello")
                    s[m][k] = s[m-1][k]
                else:
                    print("Hello THere")
                    s[m][k] = m
                DRmList = []
            #community numbering begins from 0 
            j = s[M][k] - 1
            print(j)
            for x in range(0, len(comms[j])):
                umaxTempList = Ij[j] + [comms[j][x]]
                jUnion = linear_threshold(G,umaxTempList,steps = -4)
                jnoUnion = linear_threshold(G,Ij[j],steps = -4)
                jVaU = calculateNodes(jUnion,G)
                jVa = calculateNodes(jnoUnion,G)
                jDiff = jVaU/N - jVa/N
                maxList.extend([jDiff])
            if not maxList:
                continue
            else:
                m = max(maxList)
            index = [i for i, j in enumerate(maxList) if j == m]
            newIndex = random.choice(index)
            Ij[j].extend([comms[j][newIndex]])
            I.extend([comms[j][newIndex]])
            comms[j].remove(comms[j][newIndex])
            maxList = []
        return I
    else:
        print ("ERROR: K must be lower or equal to the number of nodes")
        sys.exit()

