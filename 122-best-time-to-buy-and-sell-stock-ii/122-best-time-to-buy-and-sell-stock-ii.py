class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_ += prices[i]-prices[i-1]
        
        return max_