class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        ans=0
        pre_sum=0
        for i in nums:
            pre_sum=(pre_sum+i)%k
            if pre_sum in d:
                ans+=d[pre_sum]
                d[pre_sum]+=1
            else:
                d[pre_sum]=1
            
        return ans