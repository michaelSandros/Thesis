import community
import random
import sys
import operator
from math import *
from myGraph import *
from calculateNodes import *
from linear_threshold import *
from independent_cascade import *
import networkx as nx
import math as math

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

def perComm(G,comms,e,wholeGraph,flag,K):
    # lists
    interComms = []
    interComms.extend(comms[e])
    Ij = []
    d = {}
    NoN = wholeGraph.number_of_nodes()
    N = G.number_of_nodes()
    maxList = []
    # if K >= N then the seeders are all the nodes of the community e
    if K >= N:
        Ij = interComms
    else:
        for i in range(0,K):
            for x in range(0,len(interComms)):
                # new node
                u = interComms[x]
                # union
                temp = Ij + [u]
                # linear threshold model or independent cascade
                if flag == 1:
                    union = linear_threshold(G,temp, steps = -4)
                    noUnion = linear_threshold(wholeGraph,Ij,steps = -4)
                else:
                    union = independent_cascade(G,temp, steps = -4)
                    noUnion = independent_cascade(wholeGraph,Ij,steps = -4)
                # calculate nodes that have been activated in the community
                unionTotal = communityCalculation(comms, e, union)
                total = calculateNodes(noUnion, wholeGraph)
                d[interComms[x]] = unionTotal/NoN - total/NoN
            # return the max value of the dictionary
            highest = max(d.values())
            # return a list of nodes that have the max value
            maxList = [k for k,v in d.items() if v == highest]
            # get a random node
            umax = random.choice(maxList)
            Ij = Ij + [umax]
            d = {}
            interComms.remove(umax)
    return Ij
	
# return the communities with the biggest density
def communityDensity(G,comms):
    dens = {}
    finalList = []
    # find the density of each community
    # H is a subgraph consisting only by the nodes and the edges of each community
    for e in range(0,len(comms)):
        H = G.subgraph(comms[e])
        dens[e] = nx.density(H)
    # get values
    dens_values = list(dens.values())
    # sorted by descending order
    sorted_dens = sorted(dens_values, reverse = True)
    # community keys by descending density 
    for k in range(0,len(sorted_dens)):
        # get the key of the maximum density in each step
        key = list(dens.keys())[list(dens.values()).index(sorted_dens[k])]
        finalList.extend([key])
        # delete keys to prevent the appereance of the same community multiple times
        del dens[key]
    return finalList

def initialNodesMapping(N,topComms,comms):
    # number of the communities
    c = len(comms)
    lamda = 1
    # initial nodes per community
    initial = {}
    weights = []
    K = N
    # initialization with 0 
    for x in range(0,len(topComms)):
        initial[topComms[x]] = 0
    # initialazation of the weights: wk = (lamda^k/k!)*e^(-lamda)
    for k in range(0,len(topComms)):
        weight = (math.pow(lamda,k)/factorial(k))*math.exp(-lamda)
        weights.extend([weight])
    # while there are initial nodes
    while K > 0:
        # according to community density
        for x in range(0,len(topComms)):
            # total initial nodes per community
            k = math.ceil((K/c)*weights[x])
            # increment initial nodes per community
            initial[topComms[x]] = initial[topComms[x]] + k
            # initial nodes decrement
            K = K - k
    return initial

def commBorda(H,comms,x):
    # initial dictionaries
    ddc = {}
    dcc = {}
    dbc = {}
    ddcList = []
    dccList = []
    dbcList = []
    dc = {}
    bc = {}
    cc = {} 
    finalList = []
    total = {}
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
        # delete keys to prevent the appearance of the same node multiple times
        del ddc[key]
    for k in range(0,len(sorted_dcc)):
        key = list(dcc.keys())[list(dcc.values()).index(sorted_dcc[k])]
        dccList.extend([key])
        # delete keys to prevent the appearance of the same node multiple times
        del dcc[key]
    for k in range(0,len(sorted_dbc)):
        key = list(dbc.keys())[list(dbc.values()).index(sorted_dbc[k])]
        dbcList.extend([key])
        # delete keys to prevent the appearance of the same node multiple times
        del dbc[key]
    votes = len(comms[x]) - 1
    # votes acoring to position of each node
    for k in range(0,len(ddcList)):
        totalVotes = votes - k
        dc[ddcList[k]] = totalVotes
    for k in range(0,len(dbcList)):
        totalVotes = votes - k
        bc[dbcList[k]] = totalVotes
    for k in range(0,len(dccList)):
        totalVotes = votes - k
        cc[dccList[k]] = totalVotes
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
