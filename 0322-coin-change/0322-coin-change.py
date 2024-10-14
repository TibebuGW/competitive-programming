class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        
        @lru_cache(None)
        def dp(idx = 0, total = amount):
            if idx == len(coins):
                return float('inf')
            if total == 0:
                return 0
            
            not_take = dp(idx + 1, total)
            take = float('inf')
            if total >= coins[idx]:
                take = dp(idx, total - coins[idx]) + 1
            
            return min(take, not_take)
        
        ans = dp()
        return ans if ans != float('inf') else -1