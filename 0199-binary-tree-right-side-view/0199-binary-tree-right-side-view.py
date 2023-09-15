# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return []
        lst=[]
        q=[root]
        while q:
            lvl=[]
            for i in range(len(q)):
                curr=q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvl.append(curr.val)
            lst.append(lvl)
        return [lst[i][-1] for i in range(len(lst))]