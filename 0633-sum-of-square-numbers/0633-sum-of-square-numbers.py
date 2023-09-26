class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        n=ceil(math.sqrt(c))
        for i in range(n):
            if math.sqrt(c-i*i).is_integer():
                return True
        return False