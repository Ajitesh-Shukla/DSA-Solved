class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''Tabulate'''
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[-1][-1]=1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1<m:
                    dp[i][j]+=dp[i+1][j]
                if j+1<n:
                    dp[i][j]+=dp[i][j+1]

        return dp[0][0]

        # '''Returns num of paths from a particular m, n'''
        # dp=[[-1 for i in range(n)] for j in range(m)]
        # dp[-1][-1]=1
        # def num_paths(i, j):
        #     if i>=m or j>=n:
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     num_path=0
        #     num_path+=num_paths(i+1, j)
        #     num_path+=num_paths(i, j+1)
        #     dp[i][j]=num_path
        #     return dp[i][j]
        
        # return num_paths(0, 0)
            

