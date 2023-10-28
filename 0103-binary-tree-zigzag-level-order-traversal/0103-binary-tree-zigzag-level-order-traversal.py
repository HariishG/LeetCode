# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not(root):
            return []
        queue=[root]
        ans=[]
        level=1
        while queue:
            lvl=[]
            for i in range(len(queue)):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                lvl.append(curr.val)
            if level%2==0:
                ans.append(lvl[::-1])
            else:
                ans.append(lvl)
            level+=1
        return ans