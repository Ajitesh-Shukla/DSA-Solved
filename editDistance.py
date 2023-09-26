class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''DP'''
        dp=[[-1 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][-1]=len(word2)-i
        for j in range(len(word1)):
            dp[-1][j]=len(word1)-j

        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word2[i]==word1[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]



        '''Bruteforce will be with three operations -> Memoization 
        (gives good results but still try dp for practice'''
        # dp={}
        # def bf(i, j):
        #     if i==len(word1) and j==len(word2):
        #         return 0
        #     if i==len(word1):   # All insert operations
        #         return len(word2)-j
        #     if j==len(word2):   # All delete operations
        #         return len(word1)-i
            
        #     if (i, j) in dp.keys():
        #         return dp[(i, j)]
            
        #     if word1[i]==word2[j]:  # If equal, just move to the next one
        #         dp[(i, j)]=bf(i+1, j+1)
        #         return dp[(i, j)]
        #     else:   # Else do all three operations, and take the min
        #         len_insert=1+bf(i, j+1)
        #         len_del=1+bf(i+1, j)
        #         len_replace=1+bf(i+1, j+1)
        #         dp[(i, j)]=min(len_insert, len_del, len_replace)
        #         return dp[(i, j)]
        # return bf(0, 0)