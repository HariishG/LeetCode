class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def func(i, Or):
            if i==len(nums):
                if Or==max_or:
                    return 1
                return 0
            return func(i+1, Or)+func(i+1, Or|nums[i])

        max_or=0
        for i in nums:
            max_or|=i 
                
        return func(0,0)