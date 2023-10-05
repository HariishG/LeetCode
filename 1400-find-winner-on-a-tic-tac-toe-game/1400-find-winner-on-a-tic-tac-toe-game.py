class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # grid=[]
        # for i in range(3):
        #     t=[]
        #     for j in range(3):
        #         t.append(0)
        #     grid.append(t)
        grid=[[' ' for i in range(3)]for j in range(3)]
        letter='X'
        for i in moves:
            grid[i[0]][i[1]]=letter
            print(grid)
            if letter=='X':
                letter='O'
            else:
                letter='X'
            ans=self.findWinner(grid)
            if ans!=None:
                if ans=='X':
                    return 'A'
                return 'B'
        if len(moves)>=9:
            return 'Draw'
        return 'Pending'

    def findWinner(self, grid):
        for i in range(3):
            if grid[i][0]==grid[i][1]==grid[i][2]!=' ':
                return grid[i][0]
            if grid[0][i]==grid[1][i]==grid[2][i]!=' ':
                return grid[0][i]
        if grid[0][0]==grid[1][1]==grid[2][2]!=' ' or grid[0][2]==grid[1][1]==grid[2][0]!=' ':
            return grid[1][1]
        return None