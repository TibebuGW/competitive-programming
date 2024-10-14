class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(total = 0):
            if total == n:
                return 1
            
            if total > n:
                return 0
            
            return dp(total + 1) + dp(total + 2)
        
        return dp()