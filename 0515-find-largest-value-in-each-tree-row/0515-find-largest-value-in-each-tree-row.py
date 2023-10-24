# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return None
        queue=[root]
        ans=[]
        while queue:
            curr_lvl=[]
            for i in range(len(queue)):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr_lvl.append(curr.val)
            ans.append(max(curr_lvl))
        return ans