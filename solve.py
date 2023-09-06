# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import bestTime2BuySellCooldown
c=bestTime2BuySellCooldown.Solution()
prices = [1,2,3,0,2]
ans=c.maxProfit(prices)
print(ans)
