class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        ans=[i for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n//i+1):
                ans[i*j]=min(ans[i*j], ans[i]+j)
        return ans[-1]