class Solution:
    def minEnd(self, n: int, x: int) -> int:
        rem=n-1
        res=x
        for i in range(64):
            if x&1<<i==0:
                if rem%2==1:
                    res|=1<<i
                rem>>=1
        return res