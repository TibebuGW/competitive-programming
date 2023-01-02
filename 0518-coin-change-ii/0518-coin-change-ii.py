class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        @lru_cache(None)
        def dp(idx = n - 1, total = amount):
            
            if total == 0:
                return 1
            
            if idx == 0:
                if total % coins[idx] == 0:
                    return 1
                return 0
            
            
            not_take = dp(idx - 1, total)
            take = 0
            if total >= coins[idx]:
                take = dp(idx, total - coins[idx])
            
            return not_take + take
        
        return dp()