class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]
        
        for start, end in intervals:
            if start <= newInterval[0] <= end:
                new_interval_start = start
                break
            elif newInterval[0] < start:
                new_interval_start = newInterval[0]
                break
        
        for start, end in intervals:
            if start <= newInterval[1] <= end:
                new_interval_end = end
                break
            elif newInterval[1] < start:
                new_interval_end = newInterval[1]
                break
        
        inserted = False
        
        def overlap(s1, e1, s2, e2):
            return s1 <= e2 and s2 <= e1
        
        updated_interval = []
        if intervals and newInterval[1] < intervals[0][0]:
            updated_interval.append(newInterval)
            inserted = True
            
        for start, end in intervals:
            if overlap(start, end, new_interval_start, new_interval_end):
                if not inserted:
                    updated_interval.append([new_interval_start, new_interval_end])
                    inserted = True
            else:
                if new_interval_end < start:
                    if not inserted:
                        updated_interval.append([new_interval_start, new_interval_end])
                        inserted = True
                updated_interval.append([start, end])
        
        if not inserted:
            updated_interval.append(newInterval)
        
        return updated_interval