# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=[root]
        level=0
        while q:
            nodes=[]
            values=[]
            for i in range(len(q)):
                curr=q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                nodes.append(curr)
                values.append(curr.val)
            if level%2==1:
                for i in range(len(nodes)):
                    nodes[i].val=values[-i-1]
            level+=1
        return root