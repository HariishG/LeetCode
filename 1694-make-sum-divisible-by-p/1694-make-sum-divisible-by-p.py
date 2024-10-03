class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        Sum=sum(nums)
        rem=Sum%p
        if rem==0:
            return 0
        res=len(nums)
        d={0:-1}
        curr=0
        for i in range(len(nums)):
            curr=(curr+nums[i])%p
            req=(curr-rem)%p
            if req in d:
                res=min(res, i-d[req])
            d[curr]=i

        return res if res<len(nums) else -1
            
