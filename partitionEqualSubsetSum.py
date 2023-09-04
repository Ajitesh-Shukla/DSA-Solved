class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        tot=sum(nums)
        if tot%2==1:
            return False
        
        '''Bruteforce'''
        def get_part(i, cur_sum):
            if cur_sum>tot//2 or i>=len(nums):
                return False
            if cur_sum==tot//2:
                return True
            
            for j in range(i+1, len(nums)):
                if get_part(j, cur_sum+nums[j]):
                    return True
            return False
        
        for i in range(len(nums)):
            if get_part(i, nums[i]):
                return True
        return False

