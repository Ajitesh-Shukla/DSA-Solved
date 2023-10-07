class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        '''See limits of i, j and corner cases in these questions very carefully
        cornercase0 and cornercasen, the start and stop of iteration'''
        i, j = 0, 0
        cur_sum=nums[0]
        min_len=len(nums)+1
        while j<len(nums) and i <len(nums):
            while i<len(nums)-1 and cur_sum<target:
                i+=1
                cur_sum+=nums[i]
            if cur_sum>=target:
                min_len=min(min_len, i-j+1)
            cur_sum-=nums[j]
            j+=1
        return min_len if min_len<=len(nums) else 0
            
            

