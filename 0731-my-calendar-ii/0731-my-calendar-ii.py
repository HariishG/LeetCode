class MyCalendarTwo:

    def __init__(self):
        self.nonOverlapping=[]
        self.overlapping=[]

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not(start>=e or end<=s):
                return False
        
        for s, e in self.nonOverlapping:
            if not(start>=e or end<=s):
                self.overlapping.append((max(s, start), min(e, end)))
        self.nonOverlapping.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)