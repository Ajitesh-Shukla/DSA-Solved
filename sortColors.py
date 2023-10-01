class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''get all 0s to one side'''
        i,j=0,0
        '''i takes the first element not 0, and j moves in search of zero after it'''
        while i<len(nums) and j<len(nums):
            if nums[i]==0:
                i+=1
            else:
                j=max(j, i+1)
                while j<len(nums):
                    if nums[j]==0:
                        nums[i], nums[j]=nums[j], nums[i]
                        break
                    j+=1
        '''reverse this for 2'''
        i, j=len(nums)-1, len(nums)-1
        while i>-1 and j>-1:
            if nums[i]==2:
                i-=1
            else:
                j=min(j, i-1)
                while j>-1:
                    if nums[j]==2:
                        nums[i], nums[j]=nums[j], nums[i]
                        break
                    j-=1 
        print(nums)