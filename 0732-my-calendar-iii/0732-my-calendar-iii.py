class MyCalendarThree:

    def __init__(self):
        self.map = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.map[start] += 1
        self.map[end] -= 1
        
        total_events = 0
        max_booking = 0
        for key in sorted(self.map.keys()):
            total_events += self.map[key]
            max_booking = max(max_booking, total_events)
        
        return max_booking

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)