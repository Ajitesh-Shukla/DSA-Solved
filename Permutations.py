class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def per(i):
            if i>=len(nums):
                return [[]]
            
            ans=per(i+1)
            new_ans=[]
            for j in range(len(ans)):
                for alpha in range(len(ans[j])+1):
                    copy_ans=ans[j].copy()
                    copy_ans.insert(alpha, nums[i])     # Costly operation, try to remove
                    new_ans.append(copy_ans)   
            return new_ans
        return per(0)




        # # For loop with swapping only doesn't work, we aren't getting all elements
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         nums_copy=nums.copy()
        #         nums_copy[i], nums_copy[j] = nums_copy[j], nums_copy[i]
        #         res.append(nums_copy)
        # return res