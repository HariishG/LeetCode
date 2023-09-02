class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        # a=b=c=0
        # for i in nums:
        #     if i==0:
        #         a+=1
        #     elif i==1:
        #         b+=1
        #     else:
        #         c+=1
        # for i in range(a):
        #     nums[i]=0
        # i+=1
        # for j in range(b):
        #     nums[i]=1
        #     i+=1
        # for k in range(c):
        #     nums[i]=2
        #     i+=1