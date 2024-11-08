class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        res=[]
        pre=0
        for i in range(n):
            pre^=nums[i]
            res.append(~pre&((2**maximumBit)-1))
        return res[::-1]
        