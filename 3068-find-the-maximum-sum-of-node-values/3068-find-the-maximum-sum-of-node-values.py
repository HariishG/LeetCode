class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans=sum(nums)
        op=0
        minC=1e9+1
        for i in nums:
            if i^k>i:
                ans+=(i^k)-i
                op^=1
            minC=min(minC, abs((i^k)-i))
        if op:
            return ans-minC
        return ans
