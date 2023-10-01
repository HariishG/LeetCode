class Solution:
    def reverseWords(self, s: str) -> str:
        start=i=0
        new_s=""
        n=len(s)
        while i<n:
            if s[i]==' ':
                i+=1
                continue
            else:
                start=i
                while i<n and s[i]!=' ':
                    i+=1
                new_s=s[start:i]+' '+new_s
        return new_s.rstrip(' ')