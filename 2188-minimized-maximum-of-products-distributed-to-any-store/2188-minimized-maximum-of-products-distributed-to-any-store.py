class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def func(k):
            i=0
            j=0
            dis=0
            while i<len(quantities) and j<n:
                split=quantities[i]//k
                if quantities[i]%k:
                    split+=1
                if j+split>n:
                    return False
                j+=split                
                dis+=quantities[i]
                i+=1
            return dis==total
        l=1
        r=max(quantities)
        total=sum(quantities)
        while l<=r:
            m=(l+r)//2
            if func(m):
                r=m-1
            else:
                l=m+1
        return l