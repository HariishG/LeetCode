class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def binarySearch(l, r, q):
            b=0
            while l<=r:
                m=(l+r)//2
                if items[m][0]<=q:
                    b=max(b, items[m][1])
                    l=m+1
                elif items[m][0]>q:
                    r=m-1
            return b
            

        n=len(items)
        items.sort()
        for i in range(1,n):
            items[i][1]=max(items[i-1][1],items[i][1])
        res=[]
        for i in queries:
            res.append(binarySearch(0,n-1,i))
        return res