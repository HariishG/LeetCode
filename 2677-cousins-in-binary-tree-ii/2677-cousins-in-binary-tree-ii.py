# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=deque()
        queue.append(root)
        Sum=[]
        while queue:
            level_sum=0
            for i in range(len(queue)):
                curr=queue.popleft()
                level_sum+=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            Sum.append(level_sum)
        
        queue=deque()
        queue.append(root)
        level=0
        while queue:
            for i in range(len(queue)):
                curr=queue.popleft()
                l=r=0
                if curr.left:
                    queue.append(curr.left)
                    l=curr.left.val
                if curr.right:
                    queue.append(curr.right)
                    r=curr.right.val
                if curr.left:
                    curr.left.val=Sum[level+1]-l
                    if curr.right:
                        curr.left.val-=r
                if curr.right:
                    curr.right.val=Sum[level+1]-r
                    if curr.left:
                        curr.right.val-=l
            level+=1
        root.val=0
        return root
        
                