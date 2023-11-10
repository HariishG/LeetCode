class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[grid[0][0]]
        for i in range(1, len(grid[0])):
            dp.append(dp[-1]+grid[0][i])
        for i in range(1, len(grid)):
            temp=[dp[0]+grid[i][0]]
            for j in range(1, len(grid[0])):
                temp.append(grid[i][j]+min(dp[j], temp[j-1]))
            dp=list(temp)
        return dp[-1]
