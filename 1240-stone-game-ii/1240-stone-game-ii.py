class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}
        def func(Alice, i, M): 
            if i==len(piles):
                return 0
            if (Alice, i, M) in dp:
                return dp[(Alice, i, M)]
            if Alice:
                res=0
            else:
                res=float('inf')
            total=0
            for X in range(1,2*M+1):
                if i+X-1==len(piles):
                    break
                total+=piles[i+X-1]

                if Alice:
                    res=max(res, total+func(0, i+X, max(X,M)))
                else:
                    res=min(res, func(1, i+X, max(X,M)))
            dp[(Alice, i, M)]=res
            return res
        return func(1, 0, 1)
