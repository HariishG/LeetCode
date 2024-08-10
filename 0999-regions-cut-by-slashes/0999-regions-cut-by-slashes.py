
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        matrix=[[1 for _ in range(len(grid)*3)]for _ in range(len(grid)*3)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]=='\\':
                    matrix[i*3][j*3]=0
                    matrix[i*3+1][j*3+1]=0
                    matrix[i*3+2][j*3+2]=0
                if grid[i][j]=='/':
                    matrix[i*3][j*3+2]=0
                    matrix[i*3+1][j*3+1]=0
                    matrix[i*3+2][j*3]=0
        for i in matrix:
            print(i)
        def func(i,j):
            if not(0<=i<len(matrix)) or not(0<=j<len(matrix)) or matrix[i][j]==0:
                return
            matrix[i][j]=0
            func(i, j+1)
            func(i+1, j)
            func(i, j-1)
            func(i-1, j)
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]==1:
                    func(i,j)
                    ans+=1
        return ans