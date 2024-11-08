class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        res=[0 for _ in range(n)]
        pre=0
        for i in range(n):
            pre^=nums[i]
            res[-i-1]=(~pre&((2**maximumBit)-1))
        return res
        