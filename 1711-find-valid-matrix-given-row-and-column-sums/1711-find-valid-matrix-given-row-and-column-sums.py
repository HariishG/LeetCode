class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m=len(rowSum)
        n=len(colSum)
        ans=[[0 for _ in range(n)] for _ in range(m)]
        i=0
        j=0
        while i<m and j<n:
            ans[i][j]=min(rowSum[i], colSum[j])
            if rowSum[i]==colSum[j]:
                i+=1
                j+=1
            elif rowSum[i]>colSum[j]:
                rowSum[i]-=colSum[j]
                j+=1
            else:
                colSum[j]-=rowSum[i]
                i+=1
        return ans

        
