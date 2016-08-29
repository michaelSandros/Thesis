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
