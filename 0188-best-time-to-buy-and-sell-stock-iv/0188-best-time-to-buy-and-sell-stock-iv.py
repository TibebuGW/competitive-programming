class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(index = 0, total = 0, canBuy = True):
            
            if index == n or total == k:
                return 0
            
            if canBuy:
                buy_cur = -prices[index] + dp(index + 1, total, not canBuy)
                not_buy_cur = dp(index + 1, total, canBuy)
                return max(buy_cur, not_buy_cur)
            
            sell_here = prices[index] + dp(index + 1, total + 1, not canBuy)
            not_sell_here = dp(index + 1, total, canBuy)
            return max(sell_here, not_sell_here)
        
        return dp()