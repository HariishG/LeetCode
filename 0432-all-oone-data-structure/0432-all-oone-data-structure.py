class AllOne:

    def __init__(self):
        self.d=defaultdict(int)
        self.maxHeap=[]
        self.minHeap=[]

    def inc(self, key: str) -> None:
        self.d[key]+=1
        heapq.heappush(self.maxHeap, (-self.d[key], key))
        heapq.heappush(self.minHeap, (self.d[key], key))
    def dec(self, key: str) -> None:
        self.d[key]-=1
        if not(self.d[key]):
            del self.d[key]
        else:
            heapq.heappush(self.maxHeap, (-self.d[key], key))
            heapq.heappush(self.minHeap, (self.d[key], key))

    def getMaxKey(self) -> str:
        while self.maxHeap:
            c, k = self.maxHeap[0]
            if c==-self.d[k]:
                return k
            heapq.heappop(self.maxHeap)
        return ""
    def getMinKey(self) -> str:
        while self.minHeap:
            c, k = self.minHeap[0]
            if c==self.d[k]:
                return k
            heapq.heappop(self.minHeap)
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()