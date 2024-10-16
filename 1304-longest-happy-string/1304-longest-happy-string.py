class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a:
            heapq.heappush(heap,[-a,'a'])
        if b:
            heapq.heappush(heap,[-b,'b'])
        if c:
            heapq.heappush(heap,[-c,'c'])

        res="xx"
        while heap:
            f=heapq.heappop(heap)
            if res[-1]==f[1] and res[-2]==f[1]:
                if not(heap):
                    break
                s=heapq.heappop(heap)
                res+=s[1]
                s[0]+=1
                if s[0]:
                    heapq.heappush(heap, s)
            else:
                res+=f[1]
                f[0]+=1
            if f[0]:
                heapq.heappush(heap, f)
        return res[2:]


            

