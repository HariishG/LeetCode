class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points[0])
        dp=list(points[0])
        l=[0 for _ in range(n)]
        r=[0 for _ in range(n)]
        temp=[0 for _ in range(n)]
        for i in range(1,len(points)):
            l[0]=dp[0]
            for j in range(1,n):
                l[j]=max(dp[j], l[j-1]-1)

            r[-1]=dp[-1]
            for j in range(n-2,-1,-1):
                r[j]=max(dp[j], r[j+1]-1)
            
            for j in range(n):
                temp[j]=max(l[j], r[j])+points[i][j]
            dp=list(temp)
        return max(dp)