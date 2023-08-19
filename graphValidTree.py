class Solution:
    def checkTree(self, n: int, edges: list[list[int]]) -> list[int]:
        '''To be a tree, a graph has to satisfy two things:
        Be acyclic and be connected'''
        adj_map={i: [] for i in range(n)}
        for key, val in edges:
            adj_map[key].append(val)
            adj_map[val].append(key)

        visited=set()
        all_visited=set()
        def dfs(node, parent):
            # base
            if adj_map[node]==[]:
                return True
            
            # computation
            visited.add(node)
            for elem in adj_map[node]:
                if elem !=parent:
                    if elem not in visited : 
                        if not dfs(elem, node):
                            return False
                    else:  # cycle detection
                        return False
            visited.remove(node)
            all_visited.add(node)
            return True

        res=dfs(0, None)
        if res==False:
            return False
        
        for i in range(n):
            if i not in all_visited:
                return False
        return True
            