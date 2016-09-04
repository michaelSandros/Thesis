from myGraph import *
from communities import *
import os.path
from os.path import isfile, join
from os import listdir
from math import *

# option1: random or random graph
# option2: LT or IC model
# option3: Whole or per community
# option4: CGA?
# option5: seed nodes percentage
# option6: random seed nodes or ranking 
# option7: # of simulations

while True:
    print("Press 1 to create a random graph.")
    print("Press 2 to load a file.")
    print("Press 0 to terminate the programm.")
    option1 = int(input("Please, enter an option:\n"))
    if(option1 == 1 or option1 == 2):
        if(option1 == 1):
            while True:
                Number_of_nodes = int(input("Please, enter the number of the graph nodes:\n"))
                if(Number_of_nodes > 0):
                    G,labels,listofNodes,totalInfluence = randomGraph(Number_of_nodes)
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
                break
            elif(option2 == 2):
                diffFlag = 2
                break
            else:
                print("Invalid option, please try again.\n")
        while True:
            print("Press 1 to perform the diffusion in the whole graph.")
            print("Press 2 to perform the diffusion per community.")
            option3 = int(input("Please, choose an option:\n"))
            if(option3 == 1):
                rankFlag = 1
                wholeFlag = 1
                break
            elif(option3 == 2):
                while True:
                    print("Do you want to find the most influential nodes according to the Community Greedy Algorithm?")
                    print("Press 1 for yes.")
                    print("Press 2 for no.")
                    option4 = int(input("Please, choose an option:\n"))
                    if(option4 == 1):
                        rankFlag = 0
                        break
                    elif(option4 == 2):
                        rankFlag = 1
                        wholeFlag = 0
                        break
                    else:
                        print("Invalid option, please try again.\n")
                break
            else:
                print("Invalid option, please try again.\n")
        while True:
            option5 = int(input("Τype the percentage of nodes that are the seed nodes of the diffusion.\n"))
            if(option5 > 0 and option5 <= 100):
                nodes = G.number_of_nodes()
                totalSeeds = ceil((option5/100)*nodes)
                if(rankFlag == 1):
                    while True:
                       print("Press 1 for random initial nodes.")
                       print("Press 2 for node ranking")
                       option6 = int(input("Please choose an option.\n"))
                       if(option6 == 1):
                           print("RANDOM")
                           break
                       elif(option6 == 2):
                           print("Ranking")
                           if(wholeFlag == 0):
                               print("Per comm ranking")
                           else:
                               # top seeds by borda
                               finalList = wholeBorda(G)
                               print("FROM MYGRAPH")
                               print(finalList)
                               finalList = BordaComm(G)
                               print("COMMS")
                               print(finalList)
                               # take the first totalSeeds nodes
                               topSeeds = finalList[0:totalSeeds]
                           break
                       else:
                           print("Wrong option.\n")
            else:
                print("The percentage must be bigger than 0 and lower or equal to 100.\n")
            break
        while True:
            option7 = int(input("Enter the number of simulations.\n"))
            if (option6 > 0):
                break
            else:
                print("The number of summulations must be at least 1.\n")
    elif(option1 == 0):
        print("Programm Terminated.")
        break
    else:
        print("Wrong option.\n")
    