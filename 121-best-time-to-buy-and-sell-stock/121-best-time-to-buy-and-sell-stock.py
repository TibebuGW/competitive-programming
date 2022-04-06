class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        mmin = prices[0]
        for i in range(len(prices)):
            if prices[i] < mmin:
                mmin = prices[i]
            else:
                result = max(result, prices[i]-mmin)
                
        return result