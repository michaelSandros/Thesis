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
                        for i in range(0,iterations):
                            print(i)
                            xx[i][0] = i
                            # new influences on existing edges
                            totalInfluence =  [[0] for x in range(G.number_of_nodes())]
                            for n in range(0,len(listofNodes)):
                                end = list(labels.keys())[list(labels.values()).index(listofNodes[n])]
                                totalInfluence[n][0] = checkInfluence(G,end,totalInfluence[n][0])
                                
                            totalSum1 = 0
                            totalSum2 = 0
                            totalSum3 = 0
                            totalSum4 = 0
                            totalSum5 = 0
                            
                            # for each community:
                            #   1.  find the most influential nodes
                            #   2.  perfom the diffusion
                            #   3.  calculate the number of the activated nodes from the diffusion
                            #   4.  add that number to the total number of activated nodes

                            # random Threshold
                            randomThres(G)
                            for e in range(0,len(comms)):
                                H = G.subgraph(comms[e])
                                seeds = perComm(H,comms,e,G,flag)
                                if(flag == 1):
                                    outcome = linear_threshold(H, seeds, steps = -4)
                                else:
                                    outcome = independent_cascade(H, seeds, steps = -4)
                                total = communityCalculation(comms,e,outcome)
                                totalSum1 = totalSum1 + total

                            # the threshold for i-th node is threshold/deg(i) if deg(i) != 0
                            outDegreeThres(G)
                            for e in range(0,len(comms)):
                                H = G.subgraph(comms[e])
                                seeds = perComm(H,comms,e,G,flag)
                                if(flag == 1):
                                    outcome = linear_threshold(H, seeds, steps = -4)
                                else:
                                    outcome = independent_cascade(H, seeds, steps = -4)
                                total = communityCalculation(comms,e,outcome)
                                totalSum2 = totalSum2 + total

                            # degree Centrality Threshold
                            degreeCentralityThres(G)
                            for e in range(0,len(comms)):
                                H = G.subgraph(comms[e])
                                seeds = perComm(H,comms,e,G,flag)
                                if(flag == 1):
                                    outcome = linear_threshold(H, seeds, steps = -4)
                                else:
                                    outcome = independent_cascade(H, seeds, steps = -4)
                                total = communityCalculation(comms,e,outcome)
                                totalSum3 = totalSum3 + total

                            # betweeness Centrality Threshold  
                            betweenCentralityThres(G)
                            for e in range(0,len(comms)):
                                H = G.subgraph(comms[e])
                                seeds = perComm(H,comms,e,G,flag)
                                if(flag == 1):
                                    outcome = linear_threshold(H, seeds, steps = -4)
                                else:
                                    outcome = independent_cascade(H, seeds, steps = -4)
                                total = communityCalculation(comms,e,outcome)
                                totalSum4 = totalSum4 + total

                            # mixed Centrality Threshold
                            mixedThres(G)
                            for e in range(0,len(comms)):
                                H = G.subgraph(comms[e])
                                seeds = perComm(H,comms,e,G,flag)
                                if(flag == 1):
                                    outcome = linear_threshold(H, seeds, steps = -4)
                                else:
                                    outcome = independent_cascade(H, seeds, steps = -4)
                                print(outcome)
                                total = communityCalculation(comms,e,outcome)
                                totalSum5 = totalSum5 + total

                            active1[i][0] = totalSum1 + len(outcome[0])
                            active2[i][0] = totalSum2 + len(outcome[0])
                            active3[i][0] = totalSum3 + len(outcome[0])
                            active4[i][0] = totalSum4 + len(outcome[0])
                            active5[i][0] = totalSum5 + len(outcome[0])
                        activePlot(active1,active2,active3,active4,active5,xx)
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
