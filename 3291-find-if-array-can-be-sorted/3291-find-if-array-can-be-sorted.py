class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n=len(nums)
        cnt=bin(nums[0]).count('1')
        Min=nums[0]
        Max=nums[0]
        prev_max=0
        i=0
        while i<n:
            while i<n and bin(nums[i]).count('1')==cnt:
                Min=min(Min, nums[i])
                Max=max(Max, nums[i])
                i+=1
            if Min<prev_max:
                return False
            if i<n:
                prev_max=Max
                cnt=bin(nums[i]).count('1')
                Min=nums[i]
                Max=nums[i]
        if Min<prev_max:
            return False
        return True

            