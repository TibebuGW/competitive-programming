class MyCalendarTwo:

    def __init__(self):
        self.single_booking = []
        self.double_booking = []

    def book(self, start: int, end: int) -> bool:
        for temp_start, temp_end in self.double_booking:
            if temp_start < end and start < temp_end:
                return False
        
        for temp_start, temp_end in self.single_booking:
            if temp_start < end and start < temp_end:
                self.double_booking.append((max(start, temp_start), min(end, temp_end)))
        
        self.single_booking.append((start, end))
        return True
    
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)