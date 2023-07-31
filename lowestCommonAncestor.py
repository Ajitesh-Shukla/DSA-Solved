class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        res=[None]
        def get_common(root):
            if not root:
                return False
            left_check=get_common(root.left)
            right_check=get_common(root.right)
            '''Both checks'''
            if left_check and right_check:
                res[0]=root
            '''One checks and other is the root, only valid when all are unique'''
            if (left_check or right_check) and (root.val==p.val or root.val==q.val):
                res[0]=root

            if root.val==p.val or root.val==q.val or left_check or right_check:
                return True
            
            return False
        
        get_common(root)
        return res[0]
            
