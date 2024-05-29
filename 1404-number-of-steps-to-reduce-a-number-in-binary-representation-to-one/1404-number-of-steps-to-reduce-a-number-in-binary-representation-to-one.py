class Solution:
    def numSteps(self, s: str) -> int:
        def add(s):
            n=len(s)
            for i in range(n-1,-1,-1):
                if s[i]=='0':
                    return s[:i]+'1'+s[i+1:]
                s=s[:i]+'0'+s[i+1:]
            return '1'+s
        def div(s):
            return s[:-1]
        ans=0
        while len(s)>1:
            if s[-1]=='0':
                s=div(s)
            else:
                s=add(s)
            ans+=1
        return ans