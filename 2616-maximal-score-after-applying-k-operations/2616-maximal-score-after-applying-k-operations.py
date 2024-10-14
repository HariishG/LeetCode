class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            nums[i]*=-1
        heapq.heapify(nums)
        while k:
            num=-1*heapq.heappop(nums)
            res+=num
            heapq.heappush(nums, -(ceil(num/3)))
            k-=1
        return res