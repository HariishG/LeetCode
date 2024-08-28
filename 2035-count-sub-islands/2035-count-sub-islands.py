class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid1)
        n=len(grid1[0])
        def func(i,j):
            if not(0<=i<m) or not(0<=j<n) or grid2[i][j]==0:
                return 1
            if grid1[i][j]==0:
                return 0
            grid2[i][j]=0
            return func(i-1,j)&func(i+1,j)&func(i,j-1)&func(i,j+1)
        ans=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    ans+=func(i,j)
        return ans
            