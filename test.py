from myGraph import *
import networkx as nx
from fileCopy import *
from communities import *
import matplotlib.pyplot as plt

while True:
    print("Press 1 to generate random graph.")
    print("Press 2 to load a Graph from a file.")
    print("Press 0 to terminate the programm.\n")
    num = int(input("Please enter an option.\n"))
    if num == 1 or num == 2:
        if num ==  1:
            G,labels = createGraph()
            comms,values = commNum(G)
            comms1,values = commNum(G)
            mixedThres(G)
        else:
            fileCopy()
            edges2Nodes()
            G,labels = realGraph()
            comms,values = commNum(G)
            comms1,values = commNum(G)
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
                continue
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
                    H = G.subgraph(comms[0])
                    print(comms)
                    print(comms1)
                    seeds = initialNodes(G,comms,comms1)
                    print(seeds)
                    print(comms)
                    print(comms1)
                elif (ch2 == 2):
                    print("Percentage.\n")
                else:
                    print("Wrong option.\n")
            else:
                break
    elif num == 0:
        break
    else:
        print("Wrong option.\nPlease try again.\n")
