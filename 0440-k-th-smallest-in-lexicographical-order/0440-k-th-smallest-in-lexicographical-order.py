class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr=1
        i=1

        def func(curr):
            res=0
            neigh=curr+1
            while curr<=n:
                neigh=min(n+1, neigh)
                res+=neigh-curr
                curr*=10
                neigh*=10
            return res
            

        while i<k:
            count=func(curr)
            if i+count<=k:
                curr+=1
                i+=count
            else:
                curr*=10
                i+=1

        return curr