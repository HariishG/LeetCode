class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        ans=[]
        for i in range(0, rowIndex//2+1):
            ans.append(math.comb(rowIndex, i))
        if rowIndex%2==0:
            return ans+ans[len(ans)-2::-1]
        return ans+ans[::-1]

