
class Solution:
    def productExceptSelf(self, nums):
        '''Think map as nums are very less
        Get prefix and suffix products, see pattern'''

    # Solve with no extra space, inplace
        '''No issue, just change nums, and use the other as ans'''
        ans=[1]
        alpha=1
        for i in range(len(nums)):
            alpha*=nums[i]
            ans.append(alpha)
        # ans contains prefix prod
        nums.append(1)
        alpha=1
        for i in range(len(nums)-2, -1, -1):
            alpha*=nums[i]
            nums[i]=alpha
            ans[i]=ans[i]*nums[i+1]
        return ans[:len(ans)-1]
    
        # pre_prod=[1]
        # alpha=1
        # for elem in nums:
        #     alpha*=elem
        #     pre_prod.append(alpha)
        # suf_prod=[1]
        # alpha=1
        # for elem in nums[::-1]:
        #     alpha*=elem
        #     suf_prod.append(alpha)
        # suf_prod=suf_prod[::-1].copy()

        # ans=[]
        # for i in range(len(pre_prod)-1):
        #     ans.append(pre_prod[i]*suf_prod[i+1])
        # return ans
    
        # '''Merge those two for loops into one'''
        # ans=[1]
        # alpha, beta=1
        # for i in range(len(nums)):
        #     alpha*=nums[i]
        #     beta*=nums[len(nums)-1-i]
        #     ans.append(alpha)



        



    
