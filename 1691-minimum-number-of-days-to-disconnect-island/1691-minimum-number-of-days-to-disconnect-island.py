class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def func(i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j]==0 or (i,j) in self.visited:
                return
            self.visited.add((i,j))
            func(i+1,j)
            func(i-1,j)
            func(i,j+1)
            func(i,j-1)

        def count():
            c=0
            self.visited=set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] and (i,j) not in self.visited:
                        func(i,j)
                        c+=1
            return c

        m=len(grid)
        n=len(grid[0])
        print(count())
        if count()!=1:
            return 0
        for i in range(m):
            for j in range(n):
                self.visited=set()
                if grid[i][j]:
                    grid[i][j]=0
                    if count()!=1:
                        return 1
                    grid[i][j]=1
        return 2






