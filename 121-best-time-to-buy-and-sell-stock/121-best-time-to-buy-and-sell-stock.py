class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sp = 0
        max_ = 0
        
        for i in range(len(prices)-1, -1, -1):
            if prices[i] >= sp:
                sp = prices[i]
            else:
                max_ = max(max_, sp-prices[i])
        
        return max_