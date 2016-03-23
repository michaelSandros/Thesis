def calculateNodes(p):
    print p
    #Total activated nodes
    totalActivated = 0;
    #if in the first step noone node is activated
    if (len(p[1]) == 0):
        print "All nodes stayed inactive."
    #else find how many nodes activated
    else:
        #total steps
        print "The linear threshold model ran in %d steps." %(len(p) - 1)
        #for every step find the activated nodes
        for e in range  (1,len(p)):
            for k in range (0,len(p[e])):
                totalActivated = totalActivated + 1
        print "Activated nodes by the diffusion %d." % totalActivated
        print "Total activated nodes by the diffusion and the initial node(s) %d." % (totalActivated + len(p[0]))
