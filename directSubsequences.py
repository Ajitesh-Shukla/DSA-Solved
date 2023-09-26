class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        '''dp neetcode soln, use same logic as bruteforce'''


        '''bruteforce->Memoization'''
        # dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        # def get_num(i, j):
        #     if j==len(t):
        #         return 1

        #     if i==len(s):
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]

        #     if s[i]==t[j]:
        #         dp[i][j]=get_num(i+1, j+1)+get_num(i+1, j)
        #         return dp[i][j]
        #     else:
        #         dp[i][j]=get_num(i+1, j)
        #         return dp[i][j]
        # return get_num(0, 0)