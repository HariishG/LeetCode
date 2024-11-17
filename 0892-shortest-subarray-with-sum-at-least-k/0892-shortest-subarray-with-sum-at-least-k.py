class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        queue=deque()
        pre=0
        res=n+1
        queue.append((-1,0))
        for r in range(n):
            pre+=nums[r]
            while queue and queue[-1][1] >= pre:
                queue.pop()

            queue.append((r, pre))
            while queue and pre-queue[0][1] >= k:
                res=min(res, r-queue[0][0])
                queue.popleft()
        
        if res==n+1:
            return -1
        return res
            

