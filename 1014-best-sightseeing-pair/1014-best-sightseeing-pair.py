class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = (values[0], 0)
        ans = 1
        for i in range(1, len(values)):
            current = (values[i], i)
            ans = max(ans, dp[0]+current[0]-(i-dp[1]))
            if current[0] >= dp[0]:
                dp = current
            else:
                dp = current if i-dp[1] > dp[0]-current[0] else dp
            
            
        return ans