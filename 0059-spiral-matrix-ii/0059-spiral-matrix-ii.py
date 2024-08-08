class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[None for _ in range(n)]for _ in range(n)]
        val=1
        for i in range(n):
            ans[0][i]=val
            val+=1
        st=n-1
        i=0
        j=n-1
        while val<=n*n:
            for _ in range(st):
                i+=1
                ans[i][j]=val
                val+=1
            for _ in range(st):
                j-=1
                ans[i][j]=val
                val+=1
            st-=1
            for _ in range(st):
                i-=1
                ans[i][j]=val
                val+=1
            for _ in range(st):
                j+=1
                ans[i][j]=val
                val+=1
            st-=1
        return ans