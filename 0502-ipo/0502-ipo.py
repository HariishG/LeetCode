class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        lst=[]
        for i in range(n):
            lst.append((capital[i],profits[i]))
        lst.sort()
        i=0
        queue=[]
        for _ in range(k):
            while i<n and lst[i][0]<=w:
                heapq.heappush(queue,-lst[i][1])
                i+=1
            if not queue:
                return w
            w+=(-heapq.heappop(queue))
        return w