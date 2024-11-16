class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        n=len(nums)
        res=[-1 for _ in range(n-k+1)]
        c=1
        for i in range(1, n):
            if nums[i-1]+1==nums[i]:
                c+=1
            else:
                c=1
            if c>=k:
                res[i-k+1]=nums[i]
        return res
