class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[[1]]
        for i in range(numRows-1):
            temp=[1]
            for j in range(1,i+1):
                temp.append(lst[i][j]+lst[i][j-1])
            temp.append(1)
            lst.append(temp)
        return lst