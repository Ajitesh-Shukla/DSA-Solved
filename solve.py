# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import houseRobber
c=houseRobber.Solution()
nums = [1,2,3,1]
ans=c.rob(nums)
print(ans)
