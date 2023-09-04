class Solution:
    def reverseBits(self, n: int) -> int:
        num=0
        for i in range(32):
            num=num*10+n%2
            n//=2
        num_int=0
        i=0
        while num>0:
            num_int+=(num%10)*(2**i)
            i+=1
            num//=10
        return num_int