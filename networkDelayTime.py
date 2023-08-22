import heapq
class Solution:
    '''Cannot use prim's directly, as we cannot just add multiple scores, parallel processes are there
    Not just sequential
    Return the max shortest path from k to any other node using djikstra'''
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_map={i: [] for i in range(1, n+1)}
        for elem in times:
            adj_map[elem[0]].append((elem[2], elem[1]))

        final_scores={i: float('inf') for i in range(1, n+1)}
        final_scores[k]=0
        
        minheap=[[0, k]]
        visited=set()
        max_dist=-1

        while minheap:
            cur_score, cur_node=heapq.heappop(minheap)
            if cur_node in visited: # Single node could be there multiple times in minheap
                continue
            if cur_score>max_dist:
                max_dist=cur_score
            visited.add(cur_node)
            for score, node in adj_map[cur_node]:
                if node in visited:
                    continue
                final_scores[node]=min(final_scores[node], cur_score+score)
                heapq.heappush(minheap, [final_scores[node], node])

        if not max_dist or len(visited)!=n:
            return -1
        return max_dist







        