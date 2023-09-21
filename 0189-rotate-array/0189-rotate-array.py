class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        if k==0 or len(nums)==1:
            return
        nums[:k],nums[k:]=nums[-k:],nums[:-k]
        