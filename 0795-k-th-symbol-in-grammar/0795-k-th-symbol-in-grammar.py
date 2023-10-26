class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        start='0'
        while n>1:
            if start=='0':
                start='01'
            else:
                start='10'
            if k<=2**(n-2):
                start=start[0]
            else:
                start=start[1]
                k-=2**(n-2)
            n-=1
        return int(start)