# Imports
from linear_threshold import *
from myGraph import *
import networkx as nx
from calculateNodes import *
from communities import *

G,labels,edgeList,nodeList = customGraph()

print("Random Thresholds")
# random Thresholds
outcome1 = linear_threshold(G,[0],steps =  -4)
total1,steps1 = calculateNodes(outcome1,G)
print("Total Activated Nodes")
print(total1)
print("Total Steps")
print(steps1)
print("")

print("Threshold = Threshold/Out_degree")
# threshold(i) = threshold(i)/out_degree(i)
outDegreeThres(G)
outcome2 = linear_threshold(G,[0],steps =  -4)
total2,steps2 = calculateNodes(outcome2,G)
print("Total Activated Nodes")
print(total2)
print("Total Steps")
print(steps2)
print("")

# threshold(i) = degree_centrality(i)
print("Degree Centrality")
degreeCentralityThres(G)
outcome3 = linear_threshold(G,[0],steps =  -4)
total3,steps3 = calculateNodes(outcome3,G)
print("Total Activated Nodes")
print(total3)
print("Total Steps")
print(steps3)
print("")

# threshold(i) = betweeness_centrality(i)
print("Betweeness Centrality")
betweenCentralityThres(G)
outcome4 = linear_threshold(G,[0],steps =  -4)
total4,steps4 = calculateNodes(outcome4,G)
print("Total Activated Nodes")
print(total4)
print("Total Steps")
print(steps4)
print("")

# threshold(i) = 1/2*(betweeness_centrality(i) + degree_centrality(i))
print("Mixed Centrality")
mixedThres(G)
outcome5 = linear_threshold(G,[0],steps =  -4)
total5,steps5 = calculateNodes(outcome5,G)
print("Total Activated Nodes")
print(total5)
print("Total Steps")
print(steps5)
