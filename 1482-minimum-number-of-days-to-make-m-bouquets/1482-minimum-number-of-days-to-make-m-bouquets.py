class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n<m*k:
            return -1
        l=0
        r=max(bloomDay)
        while l<r:
            md=(l+r)//2
            b=f=0
            for i in bloomDay:
                if i<=md:
                    f+=1
                else:
                    f=0
                if f==k:
                    f=0
                    b+=1
            if b>=m:
                r=md
            else:
                l=md+1
        return l
        