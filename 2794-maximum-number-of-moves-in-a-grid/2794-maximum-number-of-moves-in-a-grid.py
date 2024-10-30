class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def func(i,j):
            if not(0<=i<m) or not(0<=j<n):
                return moves
            if (i,j) in dp:
                return dp[(i,j)]
            res=0
            if 1<=i<m and 0<=j<n-1 and grid[i][j]<grid[i-1][j+1]:
                res=max(res, 1+func(i-1, j+1))
            if 0<=j<n-1 and grid[i][j]<grid[i][j+1]:
                res=max(res, 1+func(i, j+1))
            if 0<=i<m-1 and 0<=j<n-1 and grid[i][j]<grid[i+1][j+1]:
                res=max(res, 1+func(i+1, j+1))
            dp[(i,j)]=res
            return res

        m=len(grid)
        n=len(grid[0])
        dp={}
        res=0
        for i in range(m):
            res=max(res, func(i,0))
        return res
