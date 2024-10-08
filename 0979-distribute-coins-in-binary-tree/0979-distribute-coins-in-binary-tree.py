# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not(root):
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
        
            ans+=abs(l)+abs(r)
            if root.val!=1:
                if root.val==0:
                    return l+r+1
                return l+r-(root.val-1)
            return l+r
        dfs(root)
        return ans