class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[None for _ in range(k)]
        self.front=0
        self.rear=k-1
        self.size=0
        self.maxSize=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front=(self.front-1)%self.maxSize
        self.deque[self.front]=value
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear=(self.rear+1)%self.maxSize
        self.deque[self.rear]=value
        self.size+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.maxSize
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear=(self.rear-1)%self.maxSize
        self.size-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()