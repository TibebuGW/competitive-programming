class MyCalendarTwo:

    def __init__(self):
        self.map = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.map[start] += 1
        self.map[end] -= 1
        
        total_events = 0
        for key in sorted(self.map.keys()):
            total_events += self.map[key]
            if total_events == 3:
                self.map[start] -= 1
                self.map[end] += 1
                return False
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)