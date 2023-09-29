class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.findOp(n)
    def findOp(self, num):
        if num<1:
            return float('inf')
        if num==1:
            return 0
        else:
            if num%2==0:
                return 1+self.findOp(num//2)
            return 1+min(self.findOp(num-1),self.findOp(num+1))
        