class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        @lru_cache(None)
        def dp(idx = n - 1, limit = k):
            
            if limit == 0:
                return 0
            
            if idx == 0:
                total = 0
                for i in range(min(len(piles[idx]), limit)):
                    total += piles[idx][i]
                return total
            
            not_take = dp(idx - 1, limit)
            take = 0
            total = 0
            for i in range(min(len(piles[idx]), limit)):
                num = piles[idx][i]
                total += num
                take = max(take, total + dp(idx - 1, limit - i - 1))
            
            return max(take, not_take)
    
        return dp()