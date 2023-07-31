class Solution:
    '''Single function is enough, since we need just one return type bool'''
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