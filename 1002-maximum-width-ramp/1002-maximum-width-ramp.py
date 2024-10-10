class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        max_right=[None for _ in range(n)]
        max_right[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            max_right[i]=max(nums[i], max_right[i+1])

        l=0
        res=0
        for r in range(n):
            while nums[l]>max_right[r]:
                l+=1
            res=max(res, r-l)
        return res