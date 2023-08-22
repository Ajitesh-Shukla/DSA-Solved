import heapq
class Solution:
    def dist(self, elem1, elem2):
        dist=abs(elem1[0]-elem2[0])+abs(elem1[1]-elem2[1])
        return dist

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        '''Minimum Spanning Tree Problem - Prim's algorithm
        '''   
        all_elems={}
        for i, elem in enumerate(points):
            all_elems[i]=[]
            for j, elem2 in enumerate(points):
                all_elems[i].append((j, self.dist(elem, elem2)))   # add distance of j from i 
        print(all_elems)

        visited=set()
        frontier_map=[]
        heapq.heapify(frontier_map)
        heapq.heappush(frontier_map, [0, 0])   # distance, index
        score=0

        while frontier_map:
            if len(visited)==len(points):
                return score
            cur_elem=heapq.heappop(frontier_map)
            if cur_elem[1] in visited:
                continue
            visited.add(cur_elem[1])
            score+=cur_elem[0]
            
            for elem_ in all_elems[cur_elem[1]]:
                heapq.heappush(frontier_map, [elem_[1], elem_[0]])
            
    
    # def minCostConnectPoints(self, points: list[list[int]]) -> int:
    #     '''First create a graph which has distances of all other edges as adjacency map
    #     Then do dfs: Doesn't work, can have multiple paths from a point to it's neighbors'''
    #     all_elems={}
    #     for i, elem in enumerate(points):
    #         all_elems[i]=[]
    #         for j, elem2 in enumerate(points):
    #             all_elems[i].append((j, self.dist(elem, elem2)))   # add distance of j from i 
        
    #     visited=set()
    #     min_score=[float('inf')]
    #     def dfs(node, parent, score):
    #         # base
    #         if len(visited)==len(points) and score<min_score[0]:
    #                 print(visited, score)
    #                 min_score[0]=score
    #                 return
    #         for children in all_elems[node]:
    #             if children[0]!=parent and children[0] not in visited: # Not going into same element
    #                 visited.add(children[0])
    #                 dfs(children[0], node, score+children[1])
    #                 visited.remove(children[0])
    #             # elif children[0]==parent:
    #             #     dfs(children[0], node, score)
    #             # elif children[0] in visited:   # cycle
    #             #     dfs(children[0], node, score+children[1])
    #         return 
    #     if not points:
    #         return 0
    #     dfs(0, None, 0)
    #     return min_score[0]

