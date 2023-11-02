# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.find(root, [float('-inf'), float('inf')])
    
    def find(self, root, range=None):
        if not(root.left or root.right):
            return range[0]<root.val<range[1]
        if range[0]<root.val<range[1]:
            l=True
            r=True
            if root.left:
                l=self.find(root.left, [range[0], root.val])
            if root.right:
                r=self.find(root.right, [root.val, range[1]])
            return l and r
        return False

