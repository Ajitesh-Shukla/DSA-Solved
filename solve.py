# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import wordBreak
c=wordBreak.Solution()
s = "leetcode"
wordDict = ["leet","code"]
ans=c.wordBreak(s, wordDict)
print(ans)
