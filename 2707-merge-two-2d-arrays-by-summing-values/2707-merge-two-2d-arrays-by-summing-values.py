class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i+j < len(nums1)+len(nums2):
            if i==len(nums1) or (j<len(nums2) and nums2[j][0]<nums1[i][0]):
                ans.append(nums2[j])
                j+=1
            elif j==len(nums2) or (i<len(nums1) and nums1[i][0]<nums2[j][0]):
                ans.append(nums1[i])
                i+=1
            else:
                ans.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            print(ans, i+j)
        return ans
