# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level=[]
        queue=[root]
        while queue:
            l=[]
            for i in range(len(queue)):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                l.append(curr.val)
            level.append(l)
        s=float('-inf')
        ind=1
        for i in range(len(level)):
            s_i=sum(level[i])
            if s_i>s:
                ind=i+1
                s=s_i
        return ind