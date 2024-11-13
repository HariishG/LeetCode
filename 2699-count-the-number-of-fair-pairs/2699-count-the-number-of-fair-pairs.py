class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bs1(l, r, num):
            while l<=r:
                m=(l+r)//2
                if num+nums[m]<lower:
                    l=m+1
                else:
                    r=m-1
            return l
        def bs2(l, r, num):
            while l<=r:
                m=(l+r)//2
                if num+nums[m]>upper:
                    r=m-1
                else:
                    l=m+1
            return l

        nums.sort()
        n=len(nums)
        res=0
        for i in range(n):
            lb=bs1(i+1, n-1, nums[i])
            ub=bs2(i+1, n-1, nums[i])
            if ub>lb:
                res+=ub-lb
        return res




        return res