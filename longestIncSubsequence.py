class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        '''bruteforce->dp->tabulate'''

        '''Tabulate'''
        ans=[1 for i in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            for alpha in range(j+1, len(nums)):
                if nums[alpha]>nums[j]:
                    ans[j]=max(ans[j], 1+ans[alpha])

        return max(ans)

        # '''Memoization'''
        # dp=[-1 for i in range(len(nums))]
        # def get_longest(i): # get longest one starting i
        #     if i==len(nums):
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     long_i=1
        #     for j in range(i+1, len(nums)):
        #         if nums[j]>nums[i]:
        #             long_i_j=1+get_longest(j)
        #             long_i=max(long_i, long_i_j)
        #     dp[i]=long_i
        #     return long_i
        
        # max_len=0
        # for alpha in range(len(nums)):
        #     max_len=max(max_len, get_longest(alpha))
        # return max_len

                    
