class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            nums[i]=[nums[i], bin(nums[i]).count('1')]
        for i in range(n):
            for j in range(n-i-1):
                if nums[j][0]>nums[j+1][0] and nums[j][1]==nums[j+1][1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(n-1):
            if nums[i][0]>nums[i+1][0]:
                return False
        return True