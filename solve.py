# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




import numConnectedComponents
c=numConnectedComponents.Solution()
grid =[[0, 1], [1, 2], [3, 4]]
ans=c.connectedComponents(5, grid)
print(ans)