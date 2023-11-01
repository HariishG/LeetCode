# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return []
        queue=[root]
        ans=[]
        while queue:
            for i in range(len(queue)):
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                ans.append(curr.val)
        freq=defaultdict(int)
        for i in ans:
            freq[i]+=1
        max_freq=0
        for i in freq.keys():
            if freq[i]>max_freq:
                max_freq=freq[i]
        res=[]
        for i in freq.keys():
            if freq[i]==max_freq:
                res.append(i)
        return res
    
        return max_freq_val