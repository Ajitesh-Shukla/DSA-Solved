class Solution:
    def invertTree(self, root):
        # Base Case
        if not root:
            return 
        # Compute, store temp befor changing a side
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp)
        return root