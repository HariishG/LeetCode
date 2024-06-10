class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=heights.copy()
        h.sort()
        n=len(heights)
        ans=0
        for i in range(n):
            if h[i]!=heights[i]:
                ans+=1
        return ans