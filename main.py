#Imports
from linear_threshold import *
from myGraph import *
from calculateNodes import *

G,pos,labels,edgeList,seed = createGraph()
#Call of linear_threshold - Random Euristic
randomThres = linear_threshold(G,[seed],-4)
#Call of linear_threshold - High Degree Euristic
highDegree = highDegree(G)
highDegree = linear_threshold(G,[seed],-4)

print "Random Thresholds"
calculateNodes(randomThres)
print "High Degree Thresholds"
calculateNodes(highDegree)
graphDraw(G,pos,labels,edgeList)
