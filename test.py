from myGraph import *
from fileCopy import *
from communities import *
import matplotlib.pyplot as plt

while True:
    print("Press 1 to generate random graph.")
    print("Press 2 to load a Graph from a file.")
    print("Press 0 to terminate the programm.\n")
    try :
        num = int(input("Please enter an option.\n"))
        if num == 1 or num == 2:
            if num ==  1:
                G,labels = createGraph()
                comms,values = commNum(G)
                print(comms)
            else:
                #fileCopy()
                edges2Nodes()
                G,labels = realGraph()
                comms,values = commNum(G)
                print(comms)
            while True:
                print("Press 1 for Linear Threshold Model.")
                print("Press 2 for Independent Cascade Model.")
                print("Press 3 for Community Based.")
                print("Press 0 to go back to the first menu.\n")
                ch = int(input("Please enter an option.\n"))
                if (ch == 1):
                    print("LT\n")
                    break
                elif(ch == 2):
                    print("IC\n")
                    break
                elif(ch == 3):
                    seeds = initialNodes(G,comms)
                    print(seeds)
                elif(ch == 0):
                    break
                else:
                    print("Wrong option.\nPlease try again.\n")
                    continue
            while True:
                if (ch == 1 or ch == 2):
                    print("Press 1 to implement the diffusion model in each community.")
                    print("Press 2 to implement the diffusion model in a percentage.\n")
                    ch2 = int(input("Please enter an option.\n"))
                    if (ch2 == 1):
                        for e in range(0,len(comms)):
                             subGraph = G.subgraph(comms[e])
                             print(comms[e])
                             seeds = perComm(subGraph,comms,e,G)
                             print(seeds)
                             print(comms[e])
                    elif (ch2 == 2):
                        print("Percentage.\n")
                    else:
                        print("Wrong optffion.\n")
                else:
                    break
        elif num == 0:
            break
        else:
            print("Wrong option.\nPlease try again.\n")
    except ValueError:
        print("Please give an intger.\n")
        continue
    
