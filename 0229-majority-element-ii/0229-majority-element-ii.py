class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        lst=[]
        for i in d.keys():
            if d[i]>len(nums)//3:
                lst.append(i)
        return lst