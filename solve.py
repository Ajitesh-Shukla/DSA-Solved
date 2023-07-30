# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




import LargestRectangleHistogram
c=LargestRectangleHistogram.Solution()
heights = [2,1,2]
ans=c.largestRectangleArea(heights)
print(ans)