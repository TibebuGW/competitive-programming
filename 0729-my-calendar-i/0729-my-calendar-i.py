from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        if not len(self.calendar):
            self.calendar.add((start, end))
            return True
        l = 0
        r = len(self.calendar)-1
        
        best = -1
        while l <= r:
            mid = (l+r)//2
            
            if self.calendar[mid][0] > start:
                best = mid
                r = mid - 1
            elif self.calendar[mid][0] < start:
                l = mid + 1
            else:
                return False
        
        if best == -1:
            if self.calendar[-1][0] <= start < self.calendar[-1][1]:
                return False
            else:
                self.calendar.add((start, end))
        else:
            if best == 0:
                if self.calendar[0][0] < end:
                    return False
                else:
                    self.calendar.add((start, end))
            else:
                left_nei = self.calendar[best-1]
                right_nei = self.calendar[best]
                if left_nei[1] <= start  and end <= right_nei[0]:
                    self.calendar.add((start, end))
                else:
                    return False
            
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)