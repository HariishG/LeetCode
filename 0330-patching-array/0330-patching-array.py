class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pos=1
        ans=0
        i=0
        while pos<=n:
            if i<len(nums) and nums[i]<=pos:
                pos+=nums[i]
                i+=1
            else:
                pos+=pos
                ans+=1
        return ans
