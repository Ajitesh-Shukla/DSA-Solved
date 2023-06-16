class Solution:
    def threeSum(self, nums):
        '''Use 2Sum concept and iterate over all i's, O(n^2)
        Look for O(nlogn)'''
        all_triplets=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]!=nums[i-1]:
                target=-nums[i]
                j, k=i+1, len(nums)-1
                while j<k:
                    sum_cur=nums[j]+nums[k]
                    if sum_cur<target: # Need to increment the smaller one
                        j+=1
                    elif sum_cur<target:
                        k-=1
                    elif sum_cur==target:
                        all_triplets.append([nums[i], nums[j], nums[k]])
                        while j<k and nums[j+1]==nums[j]:
                            j+=1
        return all_triplets