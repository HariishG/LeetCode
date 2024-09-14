class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Max=max(nums)
        res=1
        temp=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]==Max:
                temp+=1
            else:
                temp=1
            res=max(res, temp)
        return res