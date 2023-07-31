class Solution:
    '''Bruteforce Solution: check complete tree recursively, it works and it is like this in sol'''
    def isSameTree(self, p, q) -> bool:
        # Two base cases, either both null, or one null while other isn't
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        # compute
        left_check=self.isSameTree(p.left, q.left)
        right_check=self.isSameTree(p.right, q.right)
        if left_check and right_check and p.val==q.val:
            return True
        return False
    
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        return (self.isSameTree(root, subRoot) or self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot))