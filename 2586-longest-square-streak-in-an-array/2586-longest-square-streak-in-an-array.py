class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        uniq=set(nums)
        res=0
        for num in nums:
            curr=0
            s=num
            while s in uniq:
                curr+=1
                s*=s
            res=max(res,curr)
        if res>1:
            return res
        return -1
