class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = start = 0
        for end in range(len(prices)):
            if prices[end] < prices[start]:
                start = end
            ans = max(prices[end] - prices[start], ans)
        return ans