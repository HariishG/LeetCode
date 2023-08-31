# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return
        ans= []
        q = [root]
        ans.append([root.val])
        while q:
            level=[]
            n=len(q)
            for i in range(n):
                curr=q.pop(0)
                if curr.left:
                    level.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    q.append(curr.right)
            ans.append(level)
        return ans[-2][0]


