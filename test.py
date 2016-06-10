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

comms,values = commNum(G)
print(comms)
for e in range(0,len(comms)):
    H = G.subgraph(comms[e])
    dens[e] = nx.density(H)
print(dens)
dens1 = communityDensity(G,comms)
print(dens1)
