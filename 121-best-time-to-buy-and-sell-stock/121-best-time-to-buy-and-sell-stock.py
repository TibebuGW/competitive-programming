class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0,float('-inf')]]*2]*(len(prices)+1)
        # print(dp)
        for i in range(len(prices)):
            dp[i+1][1][0] = max(dp[i][1][0], dp[i][1][1]+prices[i])
            dp[i+1][1][1] = max(dp[i][1][1], 0-prices[i])
        # print(dp)
        return dp[-1][1][0]