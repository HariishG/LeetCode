class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        i=j=res=0
        while i<n:
            if s[i]=='0':
                res+=i-j
                j+=1
            i+=1
        return res
