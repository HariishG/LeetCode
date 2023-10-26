class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d=defaultdict(int)
        c=0
        for i in nums1:
            for j in nums2:
                d[i+j]+=1
        for k in nums3:
            for l in nums4:
                c+=d[0-(k+l)]
        return c