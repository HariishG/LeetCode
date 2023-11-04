class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l=0
        r=n
        if right:
            r=min(right)
        if left:
            l=max(left)
        return max(n-r, l)
