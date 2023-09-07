# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import targetSum
c=targetSum.Solution()
nums = [1,1,1,1,1]
target = 3
ans=c.findTargetSumWays(nums, target)
print(ans)
