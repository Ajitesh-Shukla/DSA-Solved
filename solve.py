# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import longestIncPathInMat
c=longestIncPathInMat.Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
ans=c.longestIncreasingPath(matrix)
print(ans)
