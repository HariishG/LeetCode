class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        i=len(nums1)+len(nums2)
        while i>0:
            if nums1 and nums2:
                if nums1[0]<=nums2[0]:
                    nums.append(nums1.pop(0))
                else:
                    nums.append(nums2.pop(0))
            elif nums1:
                nums+=nums1
                break
            else:
                nums+=nums2
                break
            i-=1
        i=len(nums)
        if i%2==1:
            return nums[i//2]
        return (nums[i//2]+nums[i//2-1])/2