class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m=len(nums)
        s=e=nums[0][0]
        heap=[]
        for i in range(m):
            s=min(s, nums[i][0])
            e=max(e, nums[i][0])
            heapq.heappush(heap, (nums[i][0],i,0))
        res=[s,e]  
        while True:
            num, i, j = heapq.heappop(heap)
            j+=1
            if j==len(nums[i]):
                return res
            heapq.heappush(heap, (nums[i][j], i, j))
            s=heap[0][0]
            e=max(e, nums[i][j])
            if e-s<res[1]-res[0]:
                res=[s,e]