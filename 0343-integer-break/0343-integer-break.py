class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        ans=1
        while n>=5:
            ans*=3
            n-=3
        return ans*n