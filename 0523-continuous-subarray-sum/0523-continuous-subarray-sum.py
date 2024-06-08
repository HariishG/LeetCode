class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        dic={}
        dic[0]=-1
        pre=0
        for i in range(n):
            pre=(pre+nums[i])%k
            if pre in dic:
                if i-dic[pre]>=2:
                    return True
            else:
                dic[pre]=i
        return False