class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        n1=len(s)
        n2=len(t)
        while i<n1 and j<n2:
            while i<n1 and j<n2 and s[i]==t[j]:
                i+=1
                j+=1
            i+=1
        return len(t)-j