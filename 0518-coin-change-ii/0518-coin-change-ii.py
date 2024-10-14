class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort(reverse = True)
        @lru_cache(None)
        def dp(idx = 0, total = amount):
            if idx == len(coins):
                return 0
            if total == 0:
                return 1
            
            not_take = dp(idx + 1, total)
            take = 0
            if total >= coins[idx]:
                take = dp(idx, total - coins[idx])
            
            return take + not_take
        
        return dp()