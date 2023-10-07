class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(2*n)+str(3*n)
        d=defaultdict(int)
        for i in s:
            d[i]+=1
            if i=='0' or d[i]>1:
                return False
        return True