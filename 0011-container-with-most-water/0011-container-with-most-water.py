class Solution:
    def maxArea(self, height: List[int]) -> int:
        qty=0
        i=0
        j=len(height)-1
        while i<j:
            curr_qty=(j-i)*min(height[i],height[j])
            if curr_qty>qty:
                qty=curr_qty
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return qty