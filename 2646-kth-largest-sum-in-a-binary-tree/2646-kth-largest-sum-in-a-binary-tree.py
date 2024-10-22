# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        queue=deque()
        queue.append(root)
        while queue:
            level_sum=0
            for i in range(len(queue)):
                curr=queue.popleft()
                level_sum+=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if len(heap)<k:
                heapq.heappush(heap, level_sum)
            else:
                heapq.heappush(heap, level_sum)
                heapq.heappop(heap)
        if len(heap)<k:
            return -1
        return heap[0]
            