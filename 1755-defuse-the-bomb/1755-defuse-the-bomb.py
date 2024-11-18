class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[]
        for i in range(n):
            Sum=0
            if k>0:
                for j in range(k):
                    Sum+=code[(i+j+1)%n]
            if k<0:
                for j in range(-k):
                    Sum+=code[(i-j-1)%n]
            res.append(Sum)
        return res


