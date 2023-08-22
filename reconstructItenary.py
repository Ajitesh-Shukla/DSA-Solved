class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        '''Try using dfs, O(V^2xE)->O(V^2), too much time complexity, TLE and MLE, think something else
        Changed by removing function to check all keys by keeping a track of len, and also
        enabled return type to stop iterating once answer is found
        Sort the tickets itself to get a clean code'''
        tickets=sorted(tickets, key=lambda x: x[1])
        all_map={}
        all_elem=0
        for src, dst in tickets:
            all_elem+=1
            if src in all_map:
                all_map[src].append(dst)
            else:
                all_map[src]=[dst]
        
        # for key in all_map.keys():
        #     all_map[key].sort()
        # print(all_map)

        visited=[]
        ans=[]

        def dfs(node, len_cur):
            
            # Base
            if len_cur==0:
                ans.append(visited.copy())
                return True
            
            if node not in all_map.keys():
                return False
            
            # Computation

            for i, neighbor in enumerate(all_map[node]):
                # print(neighbor)
                visited.append(neighbor)
                all_map[node].pop(i)
                res=dfs(neighbor, len_cur-1)
                if res:
                    return True
                visited.pop(-1)
                all_map[node].insert(i, neighbor)

        dfs('JFK', all_elem)

        return ['JFK']+ans[0]
            
            
