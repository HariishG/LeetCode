class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        n=len(s)
        dp=[n for _ in range(n+1)]
        dp[0]=0
        
        for i in range(1,n+1):
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i]=min(dp[i], dp[j])

            dp[i]=min(dp[i], 1+dp[i-1])
        return dp[-1]
