class Solution:
    def checkRecord(self, n: int) -> int:
        if n==1:
            return 3
        if n==2:
            return 8
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=2
        dp[2]=4
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%(10**9+7)
        ans=dp[-1]
        for i in range(n):
            ans += (dp[i] * dp[n-1-i])%(10**9+7)
        return ans%(10**9+7)