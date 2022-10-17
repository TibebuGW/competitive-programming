class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_so_far = prices[-1]
        max_ = 0
        
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > max_so_far:
                max_so_far = prices[i]
            else:
                max_ = max(max_, max_so_far-prices[i])
        
        return max_