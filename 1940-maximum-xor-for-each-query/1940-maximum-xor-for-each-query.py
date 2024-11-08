class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        def reverseBits(n):
            rev = 0
            while (n > 0):
                rev = rev << 1
                if (n & 1 == 1):
                    rev = rev ^ 1
                n = n >> 1
            return rev
        n=len(nums)
        res=[0 for _ in range(n)]
        pre=0
        for i in range(n):
            pre^=nums[i]
            k=1
            for j in range(maximumBit):
                k<<=1
                if not(pre>>j&1):
                    k|=1
            res[-i-1]=reverseBits(k)>>1
        return res
        