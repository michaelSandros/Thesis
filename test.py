from myGraph import *
from plots import *
from communities import *

G=nx.DiGraph()
labels = {}
dens = {}
for e in range(0,6):
    G.add_node(e)
    labels[e] = e

nx.set_node_attributes(G, 'activated', False)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(1,5)
G.add_edge(2,5)
G.add_edge(3,5)
G.add_edge(4,5)

'''
matching = [s for s in comms if comms[1][2] in s]
flattend = [val for comms in matching for val in comms]

print(flattend)
if comms[1][2] in flattend:
    print(comms[1][2])
    print("in")

outcome = [[0],[1,2],[3],[4,5],[]]
aN,tN = diffSizes(G,outcome)

#print(aN)
#print(tN)
'''
    

total = {}
comms,values = commNum(G)
print(comms)
dgCentrality = nx.degree_centrality(G)
bnCentrality = nx.betweenness_centrality(G)
cnCentrality = nx.closeness_centrality(G)
print(dgCentrality)
print(bnCentrality)
print(cnCentrality)


for x in range(0,len(comms)):
    for e in range(0,len(comms[x])):
        for key in dgCentrality:
            if(key == comms[x][e]):
                total[key] = dgCentrality[key] + bnCentrality[key] + cnCentrality[key]

print(total)
