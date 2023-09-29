class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.findOp(n)
    def findOp(self, num):
        if num<1:
            return float('inf')
        elif num==1:
            return 0
        elif num%2==0:
            return 1+self.findOp(num//2)
        else:
            return 1+min(self.findOp(num-1),self.findOp(num+1))
        