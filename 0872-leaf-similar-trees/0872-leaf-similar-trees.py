# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preOrder(root):
            if not(root):
                return
            if not(root.left) and not(root.right):
                lst.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        lst=[]
        preOrder(root1)
        lst1=list(lst)
        lst=[]
        preOrder(root2)
        return lst==lst1