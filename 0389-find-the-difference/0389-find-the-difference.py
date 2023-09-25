class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d=defaultdict(int)
        for i in t:
            d[i]+=1
        for i in s:
            d[i]-=1
        for i in d:
            if d[i]==1:
                return i