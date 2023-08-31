class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # Don't check in the result, high complexity
        res=[]
        nums.sort()
        cur=[]
        def sub(i):
            if i>=len(nums):
                res.append(cur.copy())
                return
            
            # Include and don't include
            # If elem at i is the same as last element in cur cur, then do not take empty  
            cur.append(nums[i])
            sub(i+1)
            cur.pop()
            if cur and nums[i]==cur[-1]:
                return
            sub(i+1)

        sub(0)
        return res

