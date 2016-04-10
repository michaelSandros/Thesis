import networkx as nx

def calculateNodes(p,G):
    # total activated nodes
    totalActivated = 0;
    totalNodes = len(G)
    if(len(p[0]) == totalNodes):
       print("All nodes were the seeders.")
    # if in the first step noone node is activated
    elif (len(p[1]) == 0):
        print ("All no seeder nodes stayed inactive.")
    # else find how many nodes activated
    else:
        # total steps
        print ("The linear threshold model ran in %d steps." %(len(p) - 1))
        # for every step find the activated nodes
        for e in range  (1,len(p)):
            for k in range (0,len(p[e])):
                totalActivated = totalActivated + 1
        print ("Activated nodes by the diffusion %d." % totalActivated)
        # message if all nodes activated
        if((totalActivated + len(p[0])) == totalNodes):
            print("All nodes activated.")
        # message if some nodes activated
        else:
            if(len(p[0]) == 1):
                print ("Total activated nodes by the diffusion and the initial node: %d" % (totalActivated + len(p[0])))
            else:
                print ("Total activated nodes by the diffusion and the initial nodes: %d" % (totalActivated + len(p[0])))
    print(p)
