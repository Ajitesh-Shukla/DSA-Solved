# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import SlidingWindowMax
c=SlidingWindowMax.Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans=c.maxSlidingWindow(nums, k)
print(ans)
