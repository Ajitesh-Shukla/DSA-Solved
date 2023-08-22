import heapq
from collections import defaultdict
from heapq import *
def djikstra_list(graph, startNode, destNode):
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

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
adj_list={}
print(djikstra_list(graph, 0, 4))
        



