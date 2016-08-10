from myGraph import *
import operator
import networkx as nx
from fileCopy import *
from linear_threshold import *
from communities import *
from independent_cascade import *
import matplotlib.pyplot as plt
from plots import *

while True:
    print("Press 1 to generate random graph.")
    print("Press 2 to load a Graph from a file.")
    print("Press 0 to terminate the programm.\n")
    num = int(input("Please enter an option.\n"))
    if num == 1 or num == 2:
        if num ==  1:
            G,labels, listofNodes = randomGraph()
            comms,values = commNum(G)
            #speed = diffSpeed(G)
        else:
            fileCopy()
            edges2Nodes()
            G,labels, listofNodes = realGraph()
            comms,values = commNum(G)
            #speed = diffSpeed(G) 
        while True:
            print("Press 1 for Linear Threshold Model.")
            print("Press 2 for Independent Cascade Model.")
            print("Press 0 to go back to the first menu.\n")
            ch = int(input("Please enter an option.\n"))
            if (ch == 1):
                flag = 1
                break
            elif(ch == 2):
                addProbs(G)
                flag = 2
                break
            elif(ch == 0):
                break
            else:
                print("Wrong option.\nPlease try again.\n")
                continue
        while True:
            if (ch == 1 or ch == 2):
                iterations = int(input("Please enter the number of iterations.\n"))
                active1 = [[0] for x in range(0,iterations)]
                active2 = [[0] for x in range(0,iterations)]
                active3 = [[0] for x in range(0,iterations)]
                active4 = [[0] for x in range(0,iterations)]
                active5 = [[0] for x in range(0,iterations)]
                xx =      [[0] for x in range(0,iterations)]
                print("Press 1 to implement the diffusion model in the whole graph.")
                print("Press 2 to implement the diffusion model in each community and merge results.")
                print("Press 3 to implement the diffusion model according to the community density.")
                print("Press 0 to go back to the first menu.\n")
                ch2 = int(input("Please enter an option.\n"))
                if (ch2 == 1):
                    print("whole")
                elif (ch2 == 2):
                    print("in each community")
                elif (ch2 == 3):
                    dens = {}
                    # find the density of each community
                    # H is a subgraph consisting only by the nodes and the edges of each community
                    for e in range(0,len(comms)):
                        H = G.subgraph(comms[e])
                        dens[e] = nx.density(H)
                    print(dens)
                    lala = communityDensity(G,comms)
                    
                    for e in range(0,len(lala)):
                        print(dens[lala[e]])
                    while True:
                        print("Press 1 to rank nodes according to centralities.")
                        print("Press 2 to rank nodes according to borda count.")
                        ch3 = int(input("Please enter an option.\n"))
                        if (ch3 == 1):
                            print("centralities")
                            break
                        elif (ch3 == 2):
                            for x in range(0,len(comms)):
                                nodes = Borda(G,comms,x)
                                print(nodes)
                            break
                        else:
                            print("Wrong option\n")
                            continue
                elif(ch2 == 0):
                    break
                else:
                    print("Wrong option.\n")
            else:
                break
    elif num == 0:
        break
    else:
        print("Wrong option.\n")
