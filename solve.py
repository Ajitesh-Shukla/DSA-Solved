# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import coinChange2
c=coinChange2.Solution()
amount = 5
coins = [1,2,5]
ans=c.change(amount, coins)
print(ans)
