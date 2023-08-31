class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        def sub(i):
            if i>=len(nums):
                return [[]]
            res=sub(i+1)
            for j in range(len(res)):
                res.append([nums[i]]+res[j])
            return res
        return sub(0)