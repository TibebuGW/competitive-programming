class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]* (len(prices)+2)
        global_max = 0
        for i in range(len(prices)-2,-1,-1):
            max_ = 0
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    max_ = max(max_, (prices[j]-prices[i])+dp[j+2])
            
            dp[i] = max(max_, dp[i+1])
        
        print(dp)
        return max(dp)