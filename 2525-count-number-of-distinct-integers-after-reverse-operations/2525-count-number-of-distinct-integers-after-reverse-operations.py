class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
            d[int(str(i)[::-1])]+=1
        return len(d)