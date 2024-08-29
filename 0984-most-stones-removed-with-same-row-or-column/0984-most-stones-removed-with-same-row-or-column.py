class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False for _ in range(n)]
        
        def dfs(stone):
            visited[stone] = True
            for nei in adj[stone]:
                if not visited[nei]:
                    dfs(nei)

        nc=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                nc+=1
        
        return n-nc
