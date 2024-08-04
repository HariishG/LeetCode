class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_sum=[]
        for i in range(n):
            temp=0
            for j in range(i,n):
                temp+=nums[j]
                sub_sum.append(temp)
        sub_sum.sort()
        return sum(sub_sum[left-1:right])%(10**9+7)