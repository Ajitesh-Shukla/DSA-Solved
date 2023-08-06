class Solution:
    def numIslands(self, grid) -> int:
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        num=[0]
        def dfs(a, b): # This function marks all the neighboring ones of a 1
            if a>=len(grid) or b>=len(grid[0]) or a<0 or b<0 or visited[a][b]==True:
                return 
            else:   # Will only enter in visited = False
                visited[a][b]=True
                if grid[a][b]=='0':
                    return
                dfs(a+1, b)
                dfs(a, b+1)
                dfs(a-1, b)
                dfs(a, b-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==False and grid[i][j]=='1':
                    '''Give recursive calls here'''
                    dfs(i, j)
                    num[0]+=1

        return num[0]




                
        

