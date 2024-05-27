class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=0
        n=len(nums)
        while j<n:
            if nums[j]!=0:
                break
            j+=1
        while i<=100 and j<n:
            if i==n-j and i<=nums[j]:
                return i
            if i==nums[j]:
                i+=1
                j+=1
            elif i<nums[j]:
                i+=1
            else:
                j+=1
        return -1