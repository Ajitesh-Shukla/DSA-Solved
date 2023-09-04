# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import partitionEqualSubsetSum
c=partitionEqualSubsetSum.Solution()
nums = [1,2,3,5]
ans=c.canPartition(nums)
print(ans)
