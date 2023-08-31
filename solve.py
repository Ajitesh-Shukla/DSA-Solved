# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import subsets2
c=subsets2.Solution()
nums = [1,2,2, 2]
ans=c.subsetsWithDup(nums)
print(ans)
