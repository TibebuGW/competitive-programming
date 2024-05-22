class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        
        for index, char in enumerate(s):
            if char in intervals:
                intervals[char][1] = index
            else:
                intervals[char] = [index, index]
        
        arr = [interval for char, interval in intervals.items()]
        arr.sort()
        merged_intervals = [arr[0]]
        for i in range(1, len(arr)):
            last_interval_start, last_interval_end = merged_intervals[-1]
            cur_interval_start, cur_interval_end = arr[i]
            
            if last_interval_start <= cur_interval_start <= last_interval_end:
                merged_intervals[-1][0] = min(last_interval_start, cur_interval_start)
                merged_intervals[-1][1] = max(last_interval_end, cur_interval_end)
            else:
                merged_intervals.append(arr[i])
        
        return [r - l + 1 for l, r in merged_intervals]