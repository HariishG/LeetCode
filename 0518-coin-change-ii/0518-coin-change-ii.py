class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0 for _ in range(amount+1)]
        temp=[None for _ in range(amount+1)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[i]=1
        for i in range(1, len(coins)):
            for j in range(amount+1):
                if j<coins[i]:
                    temp[j]=dp[j]
                else:
                    temp[j]=dp[j]+temp[j-coins[i]]
            dp=list(temp)
        return dp[-1]