class Solution:
    def overlap(self, first, second):
        if second[0] < first[1] and first[0] < second[1]:
            return True
        return False
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        last = []
        intervals.sort()
        # print(intervals)
        
        for start, end in intervals:
            if last and self.overlap(last, [start, end]):
                ans += 1
                last = [min(last[0], start), min(last[1], end)]
            else:
                last = [start, end]
        
        return ans