class MyCalendar:

    def __init__(self):
        self.events=[]

    def book(self, start: int, end: int) -> bool:
        for inter in self.events:
            if not(start>=inter[1] or end<=inter[0]):                
                return False
        self.events.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)