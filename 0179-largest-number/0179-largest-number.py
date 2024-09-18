class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x,y):
            if int(x+y)>int(y+x):
                return -1
            return 1
        nums=[str(num) for num in nums]
        nums.sort(key = cmp_to_key(cmp))
        if nums[0]=='0':
            return '0'
        return ''.join(nums)
            