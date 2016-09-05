from myGraph import *
from communities import *
from independent_cascade import *
from calculateNodes import *
import os.path
from os.path import isfile, join
from os import listdir
from math import *
from plots import *


while True:
    print("Press 1 to create a random graph.")
    print("Press 2 to load a file.")
    print("Press 0 to terminate the programm.")
    option1 = int(input("Please, choose an option:\n"))
    if(option1 == 1 or option1 == 2):
        break
    if(option1 == 0):
        print("Programm Terminated.")
        break
    else:
        print("Wrong option.\n")

if(option1 == 1 or option1 == 2):
    if(option1 == 1):
        while True:
            Number_of_nodes = int(input("Please, enter the number of the graph nodes:\n"))
            if(Number_of_nodes > 0):
                G,labels,listofNodes,totalInfluence = randomGraph(Number_of_nodes)
                randomThres(G)
                for n in range(0,len(listofNodes)):
                    end = list(labels.keys())[list(labels.values()).index(listofNodes[n])]
                    totalInfluence[n][0] = checkInfluence(G,end,totalInfluence[n][0])
                # add activation proballities for every edge
                addProbs(G)
                break
            else:
                print("Invalid option, please try again.\n")
    else:
        while True:
            path = "txtfiles/"
            # available files in the path directory
            onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
            print("Availabe files:")
            for x in range(0,len(onlyfiles)):
                print(onlyfiles[x])
            name = input("\nPlease, type the file's name:\n")
            # string concatenation 
            fname = path + name
            # does the file exist?
            # if yes
            if(os.path.isfile(fname)):
                G,labels,listofNodes,totalInfluence = realGraph(fname)
                randomThres(G)
                # total inluence for all nodes with incoming edges
                for n in range(0,len(listofNodes)):
                    end = list(labels.keys())[list(labels.values()).index(listofNodes[n])]
                    totalInfluence[n][0] = checkInfluence(G,end,totalInfluence[n][0])
                # add activation proballities for every edge
                addProbs(G)
                break
            # if no
            else:
                print("File does not exist.\n")
                onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    while True:
        print("Press 1 to implement the Linear Threshold Model.")
        print("Press 2 to implement the Indepedent Cascade Model.")
        option2 = int(input("Please, choose the diffusion model:\n"))
        if(option2 == 1):
            diffFlag = 1
        elif(option2 == 2):
            diffFlag = 2
        else:
            print("Invalid option, please try again.\n")
            continue
        while True:
            print("Press 1 to perform the diffusion in the whole graph.")
            print("Press 2 to perform the diffusion per community.")
            option3 = int(input("Please, choose an option:\n"))
            if(option3 == 1):
                rankFlag = 1
                break
            elif(option3 == 2):
                while True:
                    print("Do you want to find the most influential nodes according to the Community Greedy Algorithm?")
                    print("Press 1 for yes.")
                    print("Press 2 for no.")
                    option4 = int(input("Please, choose an option:\n"))
                    if(option4 == 1):
                        rankFlag = 0
                    elif(option4 == 2):
                        rankFlag = 1
                    else:
                        print("Invalid option, please try again.\n")
                        continue
                    break
                break
            else:
                print("Invalid option, please try again.\n")
                continue
        while True:
            option5 = int(input("Τype the percentage of nodes that are the seed nodes of the diffusion. (range: [1-100])\n"))
            if(option5 > 0 and option5 <= 100):
                nodes = G.number_of_nodes()
                totalSeeds = ceil((option5/100)*nodes)
                if(rankFlag == 1):
                    while True:
                       print("Press 1 for random initial nodes.")
                       print("Press 2 for node ranking.")
                       option6 = int(input("Please choose an option.\n"))
                       if(option6 == 1):
                           randomFlag = 1
                       elif(option6 == 2):
                           randomFlag = 0
                       else:
                           print("Invalid option, please try again.\n")
                           continue
                       break
                    break
            else:
                print("The percentage must be bigger than 0 and lower or equal to 100.\n")
                continue
        while True:
            if(randomFlag == 1):
                combinations = factorial(nodes)/(factorial(nodes - totalSeeds)*factorial(totalSeeds))
                print(combinations)
                option7 = int(input("Enter the number of simulations.\n (range [1 %d])\n"%combinations))
                if (option7 > 0 and option7 <= combinations):
                    print(option7)
                else:
                    print("The number of summulations must be at least 1.\n")
            else:
                topNodes = Borda(G)
                seedNodes = topNodes[0:totalSeeds]
                if(diffFlag == 1):
                    diffusion = linear_threshold(G,seedNodes,-4)
                else:
                    diffusion = independent_cascade(G,seedNodes,-4)
                activatedNodes, step= calculateNodes(G,diffusion)
                print(diffusion)
                stepbystep(activatedNodes,step)
            break
