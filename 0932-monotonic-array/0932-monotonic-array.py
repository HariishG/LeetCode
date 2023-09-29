class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                break
        else:
            return True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                break
        else:
            return True
        return False