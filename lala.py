from calculateNodes import *
import networkx as nx
from myGraph import *
from fileCopy import *
from linear_threshold import *
from communities import *


G,labels,listofNodes = realGraph()
comms,values = commNum(G)

for x in range(0,len(comms)):
    final = Borda(G,comms,x)
    print(final)
    
