class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq=Counter(nums)
        idx=0
        for i in range(freq[0]):
            nums[idx]=0
            idx+=1
        for i in range(freq[1]):
            nums[idx]=1
            idx+=1
        for i in range(freq[2]):
            nums[idx]=2
            idx+=1