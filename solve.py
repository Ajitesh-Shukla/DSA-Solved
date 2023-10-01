# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import spiralMatrix
c=spiralMatrix.Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans=c.spiralOrder(matrix)
print(ans)
