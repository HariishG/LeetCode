class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        Sum=mean*(len(rolls)+n)-sum(rolls)
        if Sum<n or Sum>6*n:
            return []
        ans=[1 for _ in range(n)]
        i=0
        Sum-=n
        while Sum>0:
            ans[i]+=min(5,Sum)
            Sum-=5
            i+=1
        return ans