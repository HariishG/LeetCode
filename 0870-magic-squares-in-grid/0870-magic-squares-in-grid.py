class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def func(i,j):
            if grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i+1][j]*grid[i+1][j+1]*grid[i+1][j+2]*grid[i+2][j]*grid[i+2][j+1]*grid[i+2][j+2]==362880:
                t=grid[i][j]+grid[i][j+1]+grid[i][j+2]
                if t==grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]==grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]:
                    if t==grid[i][j]+grid[i+1][j]+grid[i+2][j]==grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]==grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]:
                        if t==grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]==grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]:
                            return True
            return False

        ans=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                print(i,j)
                if func(i,j):
                    ans+=1
        return ans