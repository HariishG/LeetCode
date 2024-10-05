class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def cmp(d1,d2):
            for i in d1:
                if d1[i]!=d2[i]:
                    return False
            return True

        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        d=Counter(s2[:n1])
        d1=Counter(s1)
        if cmp(d,d1):
            return True
        for i in range(n2-n1):
            d[s2[i]]-=1
            d[s2[i+n1]]+=1
            if cmp(d,d1):
                return True
        return False