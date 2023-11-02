class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        d1=list(self.find_next(cells))
        if n==1:
            return d1
        n-=1
        c=0
        while n>0:
            cells=list(self.find_next(cells))
            c+=1
            n-=1
            if d1==cells:
                n%=c
        return cells
    def find_next(self, cells):
        temp=list(cells)
        for j in range(1,7):
            if temp[j-1]==temp[j+1]:
                cells[j]=1
            else:
                cells[j]=0
        cells[0]=cells[7]=0
        return cells


# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]   <-----
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# Day 8: [0, 0, 0, 0, 0, 1, 1, 0]
# Day 9: [0, 1, 1, 1, 0, 0, 0, 0]
# Day 10:[0, 0, 1, 0, 0, 1, 1, 0]
# Day 11:[0, 0, 1, 0, 0, 0, 0, 0]
# Day 12:[0, 0, 1, 0, 1, 1, 1, 0]
# Day 13:[0, 0, 1, 1, 0, 1, 0, 0]
# Day 14:[0, 0, 0, 0, 1, 1, 0, 0]
# Day 15:[0, 1, 1, 0, 0, 0, 0, 0]   <-----