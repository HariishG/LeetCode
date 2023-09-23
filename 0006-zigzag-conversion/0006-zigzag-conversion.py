class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[[]for i in range(numRows)]
        i=0
        while i<len(s):
            for j in range(numRows):
                if i>=len(s):
                    break
                res[j].append(s[i])
                i+=1
            for j in range(numRows-2,0,-1):
                if i>=len(s):
                    break
                res[j].append(s[i])
                i+=1
        r=''
        for i in res:
            r+=''.join(i)
        return r
