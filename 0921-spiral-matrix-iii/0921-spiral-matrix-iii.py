class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans=[]
        s=1
        while len(ans)<rows*cols:
            for _ in range(s):
                if 0<=cStart<cols and 0<=rStart<rows:
                    ans.append([rStart, cStart])
                cStart+=1
            
            for _ in range(s):
                if 0<=cStart<cols and 0<=rStart<rows:
                    ans.append([rStart, cStart])
                rStart+=1
            s+=1
            for _ in range(s):
                if 0<=cStart<cols and 0<=rStart<rows:
                    ans.append([rStart, cStart])
                cStart-=1
            
            for _ in range(s):
                if 0<=cStart<cols and 0<=rStart<rows:
                    ans.append([rStart, cStart])
                rStart-=1
            s+=1
        return ans