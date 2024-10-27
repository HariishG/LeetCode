class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        dp=[[0 for _ in range(c+1)]for _ in range(r+1)]
        ans=0
        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    dp[i+1][j+1]=min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
                    ans+=dp[i+1][j+1]
        return ans