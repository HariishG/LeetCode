# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not(root.left) and not(root.right):
            return root.val
        l=r=0
        if root.left:
            root.left.val=root.val*10+root.left.val
            l=self.sumNumbers(root.left)
        if root.right:
            root.right.val=root.val*10+root.right.val
            r=self.sumNumbers(root.right)
        return l+r
        