class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf=26000001
        n=len(original)
        adj=[[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            adj[i][i]=0
        for i in range(n):
            adj[ord(original[i])%97][ord(changed[i])%97]=min(adj[ord(original[i])%97][ord(changed[i])%97], cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if adj[i][k]+adj[k][j]<adj[i][j]:
                        adj[i][j]=adj[i][k]+adj[k][j]
        l=len(source)
        ans=0
        for i in range(l):
            if adj[ord(source[i])%97][ord(target[i])%97]==inf:
                return -1
            ans+=adj[ord(source[i])%97][ord(target[i])%97]
        return ans
