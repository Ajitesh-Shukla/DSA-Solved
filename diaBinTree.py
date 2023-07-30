max_len=0
def get_max(root):
    if not root:
        return 0
    print(root.val, max_len)
    left_len=get_max(root.left)
    right_len=get_max(root.right)
    max_cur=1+left_len+right_len
    if max_cur>max_len:
        max_len=max_cur
    return 1+max(left_len, right_len)
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        global max_len
        get_max(root)
        return max_len-1