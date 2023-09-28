class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums),2):
            for j in range(0, len(nums)-i-1, 2):
                if j+2<len(nums) and nums[j]>nums[j+2]:
                    nums[j],nums[j+2]=nums[j+2],nums[j]
        for i in range(1,len(nums),2):
            for j in range(1, len(nums)-i-1, 2):
                if j+2<len(nums) and nums[j]<nums[j+2]:
                    nums[j],nums[j+2]=nums[j+2],nums[j]
        return nums