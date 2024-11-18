class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        ans=[0 for _ in range(n)]
        if k==0:
            return ans
        if k<0:
            l=n-(-k)
            r=n
        else:
            l=1
            r=k+1
        Sum=0
        for i in range(l,r):
            Sum+=code[i]
        res=[]
        for i in range(n):
            res.append(Sum)
            Sum-=code[l%n]
            Sum+=code[r%n]
            l+=1
            r+=1
        return res


