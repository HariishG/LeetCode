class Solution:
    def minimumSteps(self, s: str) -> int:
        i=0
        n=len(s)
        while i<n and s[i]=='0':
            i+=1
        j=i
        res=0
        while i<n:
            if s[i]=='0':
                res+=i-j
                i+=1
                j+=1
            else:
                i+=1
        return res
