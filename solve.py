# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




import NoOfIslands
c=NoOfIslands.Solution()
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
ans=c.numIslands(grid)
print(ans)