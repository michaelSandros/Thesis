from myGraph import *
from calculateNodes import *

n = 5
G,labels,listofNodes,totalInfluence = randomGraph(n)
addProbs(G)
totalActive = []
for i in range(0,5):
    if(i == 0):
        outcome = [1,1]
    if(i == 1):
        outcome = [1,3,5,5]
    if(i == 2):
        outcome = [0,0]
    if(i == 3):
        outcome = [2,5,8,8]
    if(i == 4):
        outcome = [5,8,9,12,15,18,18]
    totalActive = mergeResults(totalActive,outcome)
print(totalActive)
