class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=1
        curr=nums[0]
        n=len(nums)
        i=1
        while i<n:
            if nums[i]==curr and c<2:
                c+=1
                i+=1
            elif nums[i]==curr:
                nums.pop(i)
                n-=1
            else:
                c=1
                curr=nums[i]
                i+=1