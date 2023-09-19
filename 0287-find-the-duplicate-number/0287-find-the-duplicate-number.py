class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            if d[i]==1:
                return i
            d[i]+=1
