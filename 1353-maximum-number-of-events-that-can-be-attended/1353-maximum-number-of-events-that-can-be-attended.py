from heapq import *
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        ans = 0
        total_days = max([event[1] for event in events])
        index = 0
        h = []
        
        for day in range(1, total_days + 1):
            
            while index < n and events[index][0] <= day <= events[index][1]:
                heappush(h, events[index][1])
                index += 1
            
            while h and h[0] < day:
                heappop(h)
            
            if h:
                heappop(h)
                ans += 1
        
            
        return ans