class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp=[[0 for _ in range(amount+1)]for _ in range(len(coins))]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(1, len(coins)):
            for j in range(amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[-1][-1]