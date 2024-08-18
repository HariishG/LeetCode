class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans=[1]
        visited=set()
        factors=[2,3,5]
        for i in range(n-1):
            num=heapq.heappop(ans)
            for f in factors:
                if f*num not in visited:
                    visited.add(num*f)
                    heapq.heappush(ans, num*f)
        return ans[0]
                