class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c=0
        d=defaultdict(int)
        for i in range(len(nums)):
            c+=d[nums[i]-i]
            d[nums[i]-i]+=1
        return (len(nums)*(len(nums)-1)//2) - c