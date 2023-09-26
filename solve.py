# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import editDistance
c=editDistance.Solution()
word1 = "intention"
word2 = "execution"
ans=c.minDistance(word1, word2)
print(ans)
