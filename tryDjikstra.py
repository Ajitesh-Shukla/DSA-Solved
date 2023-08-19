def djikstra(graph, startNode, destNode):
    '''Returns shortest path from given weighted graph and startNode'''
    # graph is a 2d list with weights
    shortestDist=[float('inf') for i in range(len(graph))]
    shortestDist[startNode]=0
    sptSet=[False for i in range(len(graph))]

    while not all(sptSet):
        print(shortestDist)
        minElem, minVal=None, float('inf')
        # Select the min val element O(V)
        for i, elem in enumerate(shortestDist):
            if sptSet[i]==False and elem<minVal:
                minElem=i
                minVal=elem
        sptSet[minElem]=True
        for i, weight in enumerate(graph[minElem]):
            if weight !=0 and not sptSet[i]:
                shortestDist[i]=min(shortestDist[i], shortestDist[minElem]+weight)
            
    return shortestDist[destNode]

graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(djikstra(graph, 0, 4))
        



