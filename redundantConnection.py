class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        '''dfs approach, since here we'll have two directions, 
        add a constraint about not going back to parent while identifying cycles'''
        graph_map={}
        start_key=None
        for key, val in edges:  # add both ways
            if key in graph_map.keys():
                graph_map[key].append(val)
            else:
                graph_map[key]=[val]
                start_key=key

            if val in graph_map.keys():
                graph_map[val].append(key)
            else:
                graph_map[val]=[key]
                
        visited=set()
        visited_list=[]
        ans=[]

        def dfs(node, parent):
            if node not in graph_map.keys():
                return False
            
            visited.add(node)
            visited_list.append(node)
            for elem in graph_map[node]:
                if elem!=parent:
                    if elem in visited:
                        visited_list.append(elem)
                        ans.append(visited_list)
                        return True
                    elif dfs(elem, node):
                        return True
            visited.remove(node)
            visited_list.pop()
            return False

        dfs(start_key, None)

        all_pairs=set()
        for i, elem in enumerate(ans[0]):
            if elem==ans[0][-1]:
                ans[0]=ans[0][i:]
                break

        for i in range(len(ans[0])-1):
            all_pairs.add((ans[0][i], ans[0][i+1]))
            all_pairs.add((ans[0][i+1], ans[0][i]))
        for pair in edges[::-1]:
            if (pair[0], pair[1]) in all_pairs:
                return [pair[0], pair[1]]

        return []
