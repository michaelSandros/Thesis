import community
import random
import sys
import operator
from myGraph import *
from calculateNodes import *
from linear_threshold import *
from independent_cascade import *
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
def initialNodes(G,comms,flag):
    # lists for algorithm
    I = []
    DRmList = []
    tempList = []
    umaxTempList = []
    maxList = []
    M = len(comms)
    # M empty lists
    Ij = [list([]) for _ in range(M)]
    K = 2
    # number of nodes
    N = nx.number_of_nodes(G)
    # duplicate community lists
    comms1 = duplicateComms(comms)
    if N >= K :
        # 2-d (M+1)x(K+1) arrays
        R = [[0 for x in range(K+1)] for x in range(M+1)]
        s = [[0 for x in range(K+1)] for x in range(M+1)]
        # find the K nodes with maximum influence
        for k in range(1,K+1):
            for m in range(1,M+1):
                for l in range(0,len(comms1[m-1])):
                    # union I with each node of the community
                    tempList = I + [comms1[m-1][l]]
                    # edw mallon prepei na einai ypografima
                    if (flag == 1):
                        union = linear_threshold(G,tempList,steps = -4)
                        noUnion = linear_threshold(G,I,steps = -4)
                    else:
                        union = independent_cascade(G,tempList,steps = -4)
                        noUnion = independent_cascade(G,I,steps = -4)
                    VaU = communityCalculation(comms,m-1,union)
                    Va = communityCalculation(comms,m-1,noUnion)
                    diff = VaU/N - Va/N
                    DRmList.extend([diff])
                    tempList = []
                # if the list is empty => go to the next community
                if not DRmList:
                    continue
                else:
                    DRm = max(DRmList)
                R[m][k] = max(R[m-1][k],(R[M][k-1] + DRm))
                if (R[m-1][k] >= R[M][k-1] + DRm):
                    s[m][k] = s[m-1][k]
                else:
                    s[m][k] = m
                DRmList = []
            # community numbering begins from 0
            j = s[M][k] - 1
            d = {}
            # finds the most influential node in the j-th community
            for l in range(0,len(comms1[j])):
                umaxTempList = Ij[j] + [comms1[j][l]]
                if flag == 1:
                    jUnion = linear_threshold(G,umaxTempList,steps = -4)
                    jnoUnion = linear_threshold(G,Ij[j],steps= -4)
                else:
                    jUnion = independent_cascade(G,umaxTempList,steps = -4)
                    jnoUnion = independent_cascade(G,Ij[j],steps= -4)
                jVaU = communityCalculation(comms,j,jUnion)
                jVa,steps = calculateNodes(jnoUnion,G)
                jDiff = jVaU/N - jVa/N
                d[comms1[j][l]] = jDiff
            # returns the max value of the dictionary
            highest = max(d.values())
            # returns a list of nodes that have the max value
            maxList = [k for k,v in d.items() if v == highest]
            # get a random node
            umax = random.choice(maxList)
            Ij[j] = Ij[j] + [umax]
            comms1[j].remove(umax)
            maxList = []
            umaxTempList = []
            I = I + [umax]
            d = {}
        return I
    else:
        print ("ERROR: K must be lower or equal to the number of nodes")
        sys.exit()
            
def perComm(G, comms, e, wholeGraph,flag):
    # lists
    interComms = []
    interComms.extend(comms[e])
    Ij = []
    d = {}
    K = 2
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
                if flag == 1:
                    union = linear_threshold(G,temp, steps = -4)
                    noUnion = linear_threshold(G,Ij,steps = -4)
                else:
                    union = independent_cascade(G,temp, steps = -4)
                    noUnion = independent_cascade(G,Ij,steps = -4)
                unionTotal = communityCalculation(comms,e, union)
                total, steps = calculateNodes(noUnion,wholeGraph)
                d[interComms[x]] = unionTotal/NoN - total/NoN
            # returns the max value of the dictionary
            highest = max(d.values())
            # returns a list of nodes that have the max value
            maxList = [k for k,v in d.items() if v == highest]
            # get a random node
            umax = random.choice(maxList)
            Ij = Ij + [umax]
            d = {}
            interComms.remove(umax)
    return Ij

# duplicate communities
def duplicateComms(comms):
    M = len(comms)
    # empty M list of sublists 
    comms1 = [list([]) for _ in range(M)]
    # extend each sublist in the comms1 list
    for x in range(0,len(comms)):
        # extend each element of the comms list to the new list
        for e in range(0,len(comms[x])):
            comms1[x].extend([comms[x][e]])
    return comms1

# borda counting
def Borda(G,comms,x):
    # initial dictionaries
    ddc = {}
    dcc = {}
    dbc = {}
    ddcList = []
    dccList = []
    dbcList = []
    H = G.subgraph(comms[x])
    degreeC = nx.degree_centrality(H)
    closenessC = nx.closeness_centrality(H)
    betweennessC = nx.betweenness_centrality(H)
    for l in range(0,len(comms[x])):
        ddc[comms[x][l]] = degreeC[comms[x][l]]
        dcc[comms[x][l]] = closenessC[comms[x][l]]
        dbc[comms[x][l]] = betweennessC[comms[x][l]]
        
    # get values
    ddc_values = list(ddc.values())
    dcc_values = list(dcc.values())
    dbc_values = list(dbc.values())
    
    # descending order
    sorted_ddc = sorted(ddc_values, reverse = True)
    sorted_dcc = sorted(dcc_values, reverse = True)
    sorted_dbc = sorted(dbc_values, reverse = True)
    for k in range(0,len(sorted_ddc)):
        key = list(ddc.keys())[list(ddc.values()).index(sorted_ddc[k])]
        ddcList.extend([key])
        # deletes keys to prevent the appereance of the same node multiple times
        del ddc[key]

    for k in range(0,len(sorted_dcc)):
        key = list(dcc.keys())[list(dcc.values()).index(sorted_dcc[k])]
        dccList.extend([key])
        # deletes keys to prevent the appereance of the same node multiple times
        del dcc[key]

    for k in range(0,len(sorted_dbc)):
        key = list(dbc.keys())[list(dbc.values()).index(sorted_dbc[k])]
        dbcList.extend([key])
        # deletes keys to prevent the appereance of the same node multiple times
        del dbc[key]
        
    votes = len(comms[x]) - 1

    dc = {}
    bc = {}
    cc = {}

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

    finalList = []
    total = {}
    # total votes
    for key in dc:
        total[key] = dc[key] + bc[key] + cc[key]
        
    # retun all nodes in desceding order
    total_values = list(total.values())
    sorted_total = sorted(total_values, reverse = True)
    for k in range(0,len(sorted_total)):
        key = list(total.keys())[list(total.values()).index(sorted_total[k])]
        finalList.extend([key])
        # delete keys to prevent the appereance of 2 or more same nodes
        del total[key]
    return finalList

def communityDensity(G,comms):
    dens = {}
    dens1 = {}
    densSorted = []
    finalList = []
    final_dict = {}
    for e in range(0,len(comms)):
        H = G.subgraph(comms[e])
        dens[e] = nx.density(H)
        dens1[e] = nx.density(H)
    # get values
    dens_values = list(dens.values())
    sorted_dens = sorted(dens_values, reverse = True)
    for k in range(0,len(sorted_dens)):
        key = list(dens.keys())[list(dens.values()).index(sorted_dens[k])]
        densSorted.extend([key])
        # delete keys to prevent the appereance of the same node multiple times
        del dens[key]
        
    for e in range(0,len(densSorted)):
        x = densSorted[e]
        finalList.extend([x])
    return finalList
