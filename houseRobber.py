class Solution:
    def rob(self, nums: list[int]) -> int:
        '''Unable to tabulate at first, think recursively
        Later we'll tabulate'''

        '''Tabulate, easy only, take care of computing max, store it'''
        ans=nums.copy()
        if len(nums)<=2:
            return max(nums)
        
        max_n=[-1 for i in range(len(nums))]   # Stores max value including and after this index
        max_n[-1], max_n[-2]=nums[-1], max(nums[-1], nums[-2])
        
        for i in range(len(nums)-3, -1, -1):
            # ans[i]+=max(ans[i+2:])   # Reduce the complexity of calcuulating max value, store max
            ans[i]+=max_n[i+2]  
            max_n[i]=max(ans[i], ans[i+1])   # max after and including i can be from i itself or from i+1

        return max(ans[0], ans[1])

        # '''Recursive'''
        # dp=[-1 for i in range(len(nums))]
        # if len(nums)<=2:
        #     return max(nums)
        # dp[-1]=nums[-1]
        # dp[-2]=nums[-2]

        # def loot(i):
        #     if dp[i]!=-1:
        #         return dp[i]
        #     if i>=len(nums):
        #         return 0
            
        #     max_loot=0
        #     for alpha in range(i+2, len(nums)):
        #         res=loot(alpha)
        #         if res>max_loot:
        #             max_loot=res
        #     dp[i]=max_loot+nums[i]
        #     return dp[i]
        
        # '''In every case, you need to start with either 0 or 1'''
        # return max(loot(0), loot(1))
