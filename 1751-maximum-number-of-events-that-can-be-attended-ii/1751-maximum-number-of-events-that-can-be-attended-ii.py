class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        augumented_events = events
        augumented_events.sort()
        n = len(augumented_events)
        
        @lru_cache(None)
        def dp(index = 0, limit = k, day = 0):
            if index == n or limit == 0:
                return 0
            
            l = index
            r = n - 1
            best = n
            while l <= r:
                mid = (l+r)//2
                if augumented_events[mid][0] >= day:
                    r = mid - 1
                    best = mid
                else:
                    l = mid + 1
            max_ = 0
            
            for i in range(best, n):
                cur_start, cur_end, cur_value = augumented_events[i]
                max_ = max(max_, dp(i + 1, limit - 1, cur_end + 1) + cur_value)
            
            return max_
        
        return dp()