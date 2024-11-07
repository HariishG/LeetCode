class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        set_bit=[0 for _ in range(32)]
        for i in range(32):
            for num in candidates:
                if (num>>i)%2==1:
                    set_bit[i]+=1
        return max(set_bit)
