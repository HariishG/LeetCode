class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        s=0
        e=len(self.arr)-1
        while s<=e:
            m=(s+e)//2
            if self.arr[m]==num:
                self.arr.insert(m, num)
                return
            elif self.arr[m]>num:
                e=m-1
            else:
                s=m+1
        self.arr.insert(s,num)

    def findMedian(self) -> float:
        if len(self.arr)%2==0:
            return (self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2-1])/2
        return self.arr[len(self.arr)//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()