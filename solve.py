# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




import redundantConnection
c=redundantConnection.Solution()
grid = [[1,3],[3,4],[1,5],[3,5],[2,3]]
ans=c.findRedundantConnection(grid)
print(ans)