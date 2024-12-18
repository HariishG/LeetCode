class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        for i in range(n):
            idx=abs(nums[i])
            if idx<=n and not(nums[idx-1]<0):
                nums[idx-1]*=-1
        
        for i in range(n):
            if not(nums[i]<0):
                return i+1
            
        return n+1