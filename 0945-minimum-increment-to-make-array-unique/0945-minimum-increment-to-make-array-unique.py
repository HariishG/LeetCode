class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=0
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                ans+=nums[i-1]-nums[i]+1    
                nums[i]=nums[i-1]+1    
        return ans