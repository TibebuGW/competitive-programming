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
            pick = cur_profit
            for j in range(i + 1, n):
                start, end, profit = events[j]
                if start >= cur_end:
                    pick += dp[j]
                    break
            
            dont_pick = dp[i+1]
            dp[i] = max(pick, dont_pick)
        
        return dp[0]