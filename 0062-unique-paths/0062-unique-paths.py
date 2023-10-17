class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)]for _ in range(m)]
        dp[0]=[1 for i in range(n)]
        for c in range(m):
            dp[c][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]