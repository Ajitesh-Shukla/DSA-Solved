class Solution:
    def connectedComponents(self, n: int, edges: list[list[int]]) -> list[int]:
        adj_map={i: [] for i in range(n)}
        for key, val in edges:
            adj_map[key].append(val)
            adj_map[val].append(key)
        
        visited=set()
        all_visited=set()
        
        def dfs(node, parent):
            # base
            if adj_map[node]==[]:
                return 
            
            # computation
            visited.add(node)
            for elem in adj_map[node]:
            # cycle detection, just return, no need to loop  over and over
                if elem !=parent:
                    if elem not in visited : 
                        dfs(elem, node)

            visited.remove(node)
            all_visited.add(node)
            return 
        
        ans=0
        for i in range(n):
            if i in all_visited:
                continue
            dfs(i, None)
            ans+=1
        return ans

