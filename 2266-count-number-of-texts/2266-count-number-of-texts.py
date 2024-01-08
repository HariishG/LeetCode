class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n=len(pressedKeys)
        dp=[0]*(n+1)  
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i]+=dp[i-1]
            if i-2>=0 and pressedKeys[i-1]==pressedKeys[i-2]:
                dp[i]+=dp[i-2]
                if i-3>=0 and pressedKeys[i-2]==pressedKeys[i-3]:
                    dp[i]+=dp[i-3]
                    if i-4>=0 and pressedKeys[i-3]==pressedKeys[i-4]=='7' or pressedKeys[i-3]==pressedKeys[i-4]=='9':
                        dp[i]+=dp[i-4]
        return dp[-1]%(10**9+7)