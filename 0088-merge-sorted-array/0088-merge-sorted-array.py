class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=0
        b=0
        for i in range(m,m+n):
            nums1[i]=float('inf')
        for i in range(m+n):
            if a<n and nums2[a]<=nums1[i]:
                nums1.insert(i,nums2[a])
                nums1.pop()
                a+=1
        
