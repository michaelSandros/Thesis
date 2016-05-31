from myGraph import *
import operator
import networkx as nx
from fileCopy import *
from linear_threshold import *
from communities import *
from independent_cascade import *
import matplotlib.pyplot as plt
iterations = 10
active1 = [[0] for x in range(0,iterations + 1)]
while True:
    print("Press 1 to generate random graph.")
    print("Press 2 to load a Graph from a file.")
    print("Press 0 to terminate the programm.\n")
    num = int(input("Please enter an option.\n"))
    if num == 1 or num == 2:
        if num ==  1:
            G,labels = customGraph()
            comms,values = commNum(G)
            #speed = diffSpeed(G)
        else:
            fileCopy()
            edges2Nodes()
            G,labels = realGraph()
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
                print("Press 1 to implement the diffusion model in the whole graph.")
                print("Press 2 to implement the diffusion model in each community and merge results.")
                print("Press 3 to implement the diffusion model according to the community density.")
                print("Press 0 to go back to the first menu.\n")
                ch2 = int(input("Please enter an option.\n"))
                if (ch2 == 1):
                    print("whole")
                elif (ch2 == 2):
                        for e in range(0,len(comms)):
                            H = G.subgraph(comms[e])
                            print(comms[e])
                            seeds = perComm(H,comms,e,G,flag)
                            if(flag == 1):
                                outcome = linear_threshold(H, seeds, steps = -4)
                            else:
                                outcome = independent_cascade(H, seeds, steps = -4)
                            total = communityCalculation(comms,e,outcome)
                            print(outcome)
                            print(total)
                elif (ch2 == 3):
                    dens = {}
                    # find the density of each community
                    # H is a subgraph consisting only by the nodes and the edges of each community
                    for e in range(0,len(comms)):
                        H = G.subgraph(comms[e])
                        dens[e] = nx.density(H)
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
