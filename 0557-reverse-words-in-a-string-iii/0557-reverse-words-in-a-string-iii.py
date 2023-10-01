class Solution:
    def reverseWords(self, s: str) -> str:
        start=i=0
        n=len(s)
        while i<n:
            if s[i]==' ':
                i+=1
                continue
            else:
                start=i
                while i<n and s[i]!=' ':
                    i+=1
                s=s[:start]+self.reverse(s[start:i])+s[i:]
        return s
    def reverse(self,s):
        return s[::-1]