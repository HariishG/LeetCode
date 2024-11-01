class Solution:
    def makeFancyString(self, s: str) -> str:
        res=s[:2]
        for i in range(2,len(s)):
            if res[-1]==s[i] and res[-2]==s[i]:
                continue
            res+=s[i]
        return res