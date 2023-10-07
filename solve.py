# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import minSizeSubarraySum
c=minSizeSubarraySum.Solution()
target = 11
nums = [1,1,1,1,1,1,1,1]
ans=c.minSubArrayLen(target, nums)
print(ans)
