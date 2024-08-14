class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def func(d):
            l=0
            res=0
            for i in range(len(nums)):
                while nums[i]-nums[l]>d:
                    l+=1
                res+=i-l
            return res

        l=0
        r=max(nums)
        while l<r:
            m=(l+r)//2
            pairs=func(m)
            if pairs>=k:
                r=m
            else:
                l=m+1
        return r