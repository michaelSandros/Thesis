# Imports
from linear_threshold import *
from myGraph import *
import networkx as nx
from calculateNodes import *
from communities import *

iterations = 10

G,labels = realGraph()
comms,values = commNum(G)
# random Thresholds
print("Random Thresholds")
seeds1 = initialNodes(G,comms)
print(seeds1)
outcome1 = linear_threshold(G,seeds1,steps =  -4)
print(outcome1)
total1,steps1 = calculateNodes(outcome1,G)
print("Total Activated Nodes")
print(total1)
print("Total Steps")
print(steps1)
print("")

# threshold(i) = threshold(i)/out_degree(i)
print("Threshold = Threshold/Out_degree")
outDegreeThres(G)
seeds2 = initialNodes(G,comms)
print(seeds2)
outcome2 = linear_threshold(G,seeds2,steps =  -4)
print(outcome2)
total2,steps2 = calculateNodes(outcome2,G)
print("Total Activated Nodes")
print(total2)
print("Total Steps")
print(steps2)
print("")

# threshold(i) = degree_centrality(i)
print("Degree Centrality")
degreeCentralityThres(G)
seeds3 = initialNodes(G,comms)
print(seeds3)
outcome3 = linear_threshold(G,seeds3,steps =  -4)
print(outcome3)
total3,steps3 = calculateNodes(outcome3,G)
print("Total Activated Nodes")
print(total3)
print("Total Steps")
print(steps3)
print("")

# threshold(i) = betweeness_centrality(i)
print("Betweeness Centrality")
betweenCentralityThres(G)
seeds4 = initialNodes(G,comms)
print(seeds4)
outcome4 = linear_threshold(G,seeds4,steps =  -4)
print(outcome4)
total4,steps4 = calculateNodes(outcome4,G)
print("Total Activated Nodes")
print(total4)
print("Total Steps")
print(steps4)
print("")

# threshold(i) = 1/2*(betweeness_centrality(i) + degree_centrality(i))
print("Mixed Centrality")
mixedThres(G)
seeds5 = initialNodes(G,comms)
print(seeds5)
outcome5 = linear_threshold(G,seeds5,steps =  -4)
print(outcome5)
total5,steps5 = calculateNodes(outcome5,G)
print("Total Activated Nodes")
print(total5)
print("Total Steps")
print(steps5)
print(t)
