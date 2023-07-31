import collections
class Solution:
    def levelOrder(self, root):
        '''Level order traversal->Queue'''
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)): #Using range(len(q)) fixes the range, so it doesn't changes with q
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
            
            