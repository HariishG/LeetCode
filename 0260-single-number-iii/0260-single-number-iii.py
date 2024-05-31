class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor^=i
        xor
        for i in range(32):
            if xor&(1<<i):
                last_bit=i
        n1=0
        for i in nums:
            if i&(1<<last_bit):
                n1^=i
        return (n1, xor^n1)