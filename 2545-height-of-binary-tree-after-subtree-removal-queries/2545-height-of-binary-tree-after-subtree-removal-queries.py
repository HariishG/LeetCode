# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_heights=[0]*100001
        
        def func1(root, curr):
            if not root:
                return
            max_heights[root.val]=self.curr
            self.curr=max(curr, self.curr)

            func1(root.left, curr+1)
            func1(root.right, curr+1)
        def func2(root, curr):
            if not root:
                return
            max_heights[root.val]=max(max_heights[root.val], self.curr)
            self.curr=max(curr, self.curr)

            func2(root.right, curr+1)
            func2(root.left, curr+1)
        
        self.curr=0
        func1(root, 0)
        self.curr=0
        func2(root, 0)
        return [max_heights[i] for i in queries]