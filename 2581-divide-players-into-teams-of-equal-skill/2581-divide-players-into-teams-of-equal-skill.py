class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total=sum(skill)
        n=len(skill)
        if total%(n//2)!=0:
            return -1
        req=total//(n//2)
        d=Counter(skill)
        for i in d:
            if d[i]!=d[req-i]:
                return -1
        ans=0
        for i in d:
            ans+=d[i]*i*(req-i)
        
        return ans//2