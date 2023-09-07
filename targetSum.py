import numpy as np
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        '''Tabulate'''
        if target>sum(nums):
            return 0
        dp=[[0 for i in range(2*sum(nums)+1)] for j in range(len(nums))]
        center=sum(nums)
        for i in range(2*sum(nums)+1):
            if i-center==nums[-1] or i-center==-nums[-1]:
                dp[-1][i]=1
                '''If we encounter 0, we need to double the number of cases'''
                if nums[-1]==0:
                    dp[-1][i]=2

        for i in range(len(nums)-2, -1, -1):
            for j in range(2*sum(nums)+1):
                left, right=j-nums[i], j+nums[i]
                if left>=0:
                    dp[i][j]+=dp[i+1][left]
                if right<2*sum(nums)+1:
                    dp[i][j]+=dp[i+1][right]
        return dp[0][target+center]

        # '''Recursive solution->memoization (return number of possible paths after a step and cur sum),
        # better time complexity than tabulation'''
        # dp=[[-1 for i in range(2*sum(nums)+1)] for j in range(len(nums))]  # O(sum(nums)*n)
        # print(len(dp[0]))
        # center=sum(nums)
        # def find_tar(i, cur_sum):  # cur_sum can be in -sum, +sum
        #     if i>=len(nums):
        #         if cur_sum==target:
        #             return 1
        #         else:
        #             return 0
        #     if dp[i][cur_sum+center]!=-1:
        #         return dp[i][cur_sum+center]
            
        #     nums_left=find_tar(i+1, cur_sum+nums[i])
        #     nums_right=find_tar(i+1, cur_sum-nums[i])
        #     dp[i][cur_sum+center]=nums_left+nums_right
        #     return dp[i][cur_sum+center]
        # res=find_tar(0, 0)
        # return res
        