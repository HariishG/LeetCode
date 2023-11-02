# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.find(root)[0]
    def find(self, root):
        if not(root.left or root.right):
            return [1, root.val, 1]
        temp1=[0,0,0]
        temp2=[0,0,0]
        if root.left:
            temp1=self.find(root.left)
        if root.right:
            temp2= self.find(root.right)
        if root.val==(temp1[1]+temp2[1]+root.val)//(1+temp1[2]+temp2[2]):
            return [1+temp1[0]+temp2[0], temp1[1]+temp2[1]+root.val, 1+temp1[2]+temp2[2]]
        return [temp1[0]+temp2[0], temp1[1]+temp2[1]+root.val, 1+temp1[2]+temp2[2]]