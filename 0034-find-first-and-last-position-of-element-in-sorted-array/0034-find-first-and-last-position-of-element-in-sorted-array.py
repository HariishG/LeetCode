class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findLeft(nums, target), self.findRight(nums, target)]
    def findLeft(self, nums, target):
        start=0
        end=len(nums)-1
        pos=-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                pos=mid
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return pos
    def findRight(self, nums, target):
        start=0
        end=len(nums)-1
        pos=-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                pos=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return pos
    

