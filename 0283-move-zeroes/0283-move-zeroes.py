class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        while i<len(nums)-j:
            if nums[i]==0:
                nums.append(nums.pop(i))
                j+=1
            else:
                i+=1
