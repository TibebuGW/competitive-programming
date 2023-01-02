class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        @lru_cache(None)
        def dp(idx = n - 1, total = amount):
            
            if total == 0:
                return 0
            
            if idx == 0:
                remainder = total
                if remainder % coins[idx] == 0:
                    return remainder // coins[idx]
                return float('inf')
            
            not_take = dp(idx - 1, total)
            take = float('inf')
            
            if total >= coins[idx]:
                take = 1 + dp(idx, total - coins[idx])
            
            return min(take, not_take)
        
        ans = dp()
        return ans if ans != float('inf') else -1