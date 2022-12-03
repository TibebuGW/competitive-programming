class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1]*2 for _ in range(n)]
        longest = 1
        count = 0
        
        
        for i in range(n-1, -1, -1):
            max_ = [1, 1]
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if dp[j][0] + 1 > max_[0]:
                        max_ = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == max_[0]:
                        max_[1] += dp[j][1]
            dp[i] = max_[::]
            longest = max(longest, dp[i][0])
        ans = 0
        for length, count in dp:
            if length == longest:
                ans += count
        
        return ans