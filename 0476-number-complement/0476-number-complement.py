class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        ans=0
        power=0
        for i in range(len(b)-1,-1,-1):
            if b[i]=='0':
                ans+=2**power
            power+=1
        return ans