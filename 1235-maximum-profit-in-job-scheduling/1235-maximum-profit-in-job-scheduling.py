class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # top down doesn't pass
        
        events = list(zip(startTime, endTime, profit)) 
        events.sort()
        events.append((50001,50002,0))
        n = len(events)
        dp = [0]*(n)
        
        for i in range(n-2, -1 ,-1):
            cur_start, cur_end, cur_profit = events[i]
            l = i + 1
            r = n - 1
            best = n - 1
            while l <= r:
                mid = (l+r)//2
                if events[mid][0] >= cur_end:
                    r = mid - 1
                    best = mid
                else:
                    l = mid + 1
            
            pick = cur_profit + dp[best]
            dont_pick = dp[i+1]
            dp[i] = max(pick, dont_pick)
        
        return dp[0]