class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        i=0
        j=-1
        ans=0
        cost=0
        while i<n:
            cost+=abs(ord(s[i])-ord(t[i]))
            while cost>maxCost:
                j+=1
                cost-=abs(ord(s[j])-ord(t[j]))
            ans=max(ans, i-j)
            i+=1
        return ans