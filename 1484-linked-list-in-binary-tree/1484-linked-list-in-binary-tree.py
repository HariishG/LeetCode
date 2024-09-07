# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.ans=False
        def func(root, h):
            if not(h):
                self.ans=True
                return
            if not(root):
                return
            if h.val==root.val:
                func(root.left, h.next) or func(root.right, h.next)
        def dfs(root):
            if not(root):
                return
            if self.ans==False:
                func(root, head)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.ans