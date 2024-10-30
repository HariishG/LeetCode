class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        dp_inc=[1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp_inc[i]=max(dp_inc[i], 1+dp_inc[j])
        
        dp_dec=[1 for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    dp_dec[i]=max(dp_dec[i], 1+dp_dec[j])

        res=n
        for i in range(n):
            if dp_inc[i]>1 and dp_dec[i]>1:
                res=min(res, n-dp_inc[i]-dp_dec[i]+1)
        return res
        