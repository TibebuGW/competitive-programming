class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        @lru_cache(None)
        def solve(index = 0, status = "to buy"):
            if index == n:
                return 0
            if status == "to buy":
                buy = solve(index + 1, "to sell") - prices[index]
                not_buy = solve(index + 1, "to buy")
                return max(buy, not_buy)
            else: 
                sell = prices[index]
                not_sell = solve(index + 1, status)
                return max(sell, not_sell)                
            
        return max(0, solve())