class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        tot=sum(nums)
        if tot%2==1:
            return False
        
        '''dp'''
        '''Why set works but list doesn't??? Is it the append option??? Still O(1)'''
        all_sums=set()
        all_sums.add(0)
        for i in range(len(nums)-1, -1, -1):
            set2=set()
            for elem in all_sums:
                if nums[i]+elem==tot//2:
                    return True
                elif nums[i]+elem<tot//2:
                    set2.add(nums[i]+elem)
            for elem in set2:
                all_sums.add(elem)
        return False
                

        # '''Bruteforce'''
        # def get_part(i, cur_sum):
        #     if cur_sum>tot//2 or i>=len(nums):
        #         return False
        #     if cur_sum==tot//2:
        #         return True
            
        #     for j in range(i+1, len(nums)):
        #         if get_part(j, cur_sum+nums[j]):
        #             return True
        #     return False
        
        # for i in range(len(nums)):
        #     if get_part(i, nums[i]):
        #         return True
        # return False

