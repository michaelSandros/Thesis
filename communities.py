import community

def commNum(G):
    # directed Graph to Undirected
    UG = G.to_undirected()
    # empty lists
    communities = []
    list2 = []
    # find the community that the node belongs
    partition = community.best_partition(UG)
    # get the number of each community
    values = partition.values()
    # max community number
    max_value = max(values)

    part = community.best_partition(UG)
    values = [part.get(node) for node in UG.nodes()]
    # for all communities with numbers from 0 to max_value
    for comm in range (0, max_value+1):
        # for all nodes in the graph 
        for e in UG.nodes():
            # checks if the number of the community
            # is the same with the node's community number
            if(partition[e] == comm):
                # if they match
                # put new node number in the temporary list
                list2.extend([e])
        # put the temporary list to the list
        # communities list will be:
        # [[nodes_of_community0],[nodes_of_community1],....]
        communities.append(list2)
        # delete list content
        list2 = []
        
    return (communities,values)

def initialNodes(G,comms):
    K = 4
    M = len(comms)
    seeds = []
    R = []
    s = []
    for k in range(1,K+1):
        R.append(0)
        s.append(0)
    print (R)
    return seeds

            
