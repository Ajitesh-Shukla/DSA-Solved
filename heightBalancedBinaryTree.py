class Solution:
    def isBalanced(self, root) -> bool:
        '''For a balanced height binary tree, the left and right height difference 
        should be less than equal to one, for all level nodes'''
        res=[True]
        def check_balance(root):
            if not root:
                return 0
            left_ht=check_balance(root.left)
            right_ht=check_balance(root.right)
            if abs(left_ht-right_ht)>1:
                res[0]=False
            return 1+max(left_ht, right_ht)
        check_balance(root)
        return res[0]
