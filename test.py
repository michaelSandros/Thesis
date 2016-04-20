# CGA Algorithm
def initialNodes(G,comms):
    I = []
    DRmList = []
    tempList = []
    umaxTempList = []
    maxList = []
    M = len(comms)
    Ij = [list([]) for _ in range(M)]
    K = 2
    # number of nodes
    N = nx.number_of_nodes(G)
    M = 3
    if N >= K :
        # 2-d (M+1)x(K+1) arrays
        R = [[0 for x in range(K+1)] for x in range(M+1)]
        s = [[0 for x in range(K+1)] for x in range(M+1)]
        print(comms)
        for k in range(1,K+1):
            for m in range(1,M+1):
                for l in range(0,len(comms[m-1])):
                    #union I with the influential nodes
                    tempList = I + [comms[m-1][l]]
                    # edw mallon prepei na einai ypografima
                    union = linear_threshold(G,tempList,steps = -4)
                    noUnion = linear_threshold(G,I,steps = -4)
                    VaU = calculateNodes(union,G)
                    Va = calculateNodes(noUnion,G)
                    diff = VaU/N - Va/N
                    DRmList.extend([diff])
                    tempList = []
                if not DRmList:
                    continue
                else:
                    DRm = max(DRmList)
                R[m][k] = max(R[m-1][k],R[M][k-1]+DRm)
                if (R[m-1][k] >= R[M][k-1] + DRm):
                    s[m][k] = s[m-1][k]
                else:
                    s[m][k] = m
                DRmList = []
            # community numbering begins from 0 
            j = s[M][k] - 1
            print(j)
            for x in range(0, len(comms[j])):
                umaxTempList = Ij[j] + [comms[j][x]]
                jUnion = linear_threshold(G,umaxTempList,steps = -4)
                jnoUnion = linear_threshold(G,Ij[j],steps = -4)
                jVaU = calculateNodes(jUnion,G)
                jVa = calculateNodes(jnoUnion,G)
                jDiff = jVaU/N - jVa/N
                maxList.extend([jDiff])
            if not maxList:
                continue
            else:
                m = max(maxList)
            index = [i for i, j in enumerate(maxList) if j == m]
            # random in
            newIndex = random.choice(index)
            Ij[j].extend([comms[j][newIndex]])
            I.extend([comms[j][newIndex]])
            comms[j].remove(comms[j][newIndex])
            maxList = []
        return I
    else:
        print ("ERROR: K must be lower or equal to the number of nodes")
        sys.exit()
