class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]

        dp[-1][-1]=True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                '''check right and bottom'''
                if i!=len(s1) and dp[i+1][j]==True and s3[i+j]==s1[i]: # going top
                    dp[i][j]=True
                
                elif j!=len(s2) and dp[i][j+1]==True and s3[i+j]==s2[j]: # going left
                    dp[i][j]=True
                    
        return dp[0][0]

        '''i will note the index of s1, j will s2 and s3 will be i+j
        The key here is that the extra row frequently used in dp is a must here,
        TLE for memoization, why??'''
        # if len(s1)+len(s2)!=len(s3):
        #     return False

        # dp={}
        # '''Based on our approach, we can't label a dp as true, but we can as false, think'''
          
        # def dfs(i, j):

        #     if i==len(s1) and j==len(s2):
        #         return True
            
        #     if (i, j) in dp.keys():
        #         return dp[(i, j)]

        #     left, right=False, False
        #     if i<len(s1) and s3[i+j]==s1[i]:
        #         left=dfs(i+1, j)
        #     if j<len(s2) and s3[i+j]==s2[j]:
        #         right=dfs(i, j+1)

        #     if not (left or right):
        #         dp[(i, j)]=False

        #     return (left or right)
        # res=dfs(0, 0)
        
        return res
        
          
                
