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
comms = [[0,1,2,3,4,5]]
print("before")
print(comms)
lala = perComm(G,comms,0,G,1)
lala1 = initialNodes(G,comms,1)
print("after")
print(lala)
print(lala1)
