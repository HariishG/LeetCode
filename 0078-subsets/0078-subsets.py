class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def func(i,subset):
            if i==n:
                return [subset]
            return func(i+1, subset)+func(i+1, [nums[i]]+subset)
        return func(0,[])