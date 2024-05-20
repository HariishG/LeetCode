class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def ft(i,sum):
            if i==n:
                return sum
            return ft(i+1,sum)+ft(i+1,sum^nums[i])
        return ft(0,0)