class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        dp={}
        def func(i,subset):
            if i==n:
                if len(subset)>0:
                    return 1
                return 0
            if (i,subset) in dp:
                return dp[(i,subset)]

            res=0
            if nums[i]-k not in subset:
                res+=func(i+1, subset+(nums[i],))
            res+=func(i+1, subset)
            dp[(i,subset)]=res
            return res
        return func(0,())