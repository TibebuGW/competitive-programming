class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1]*n
        total_max = 1
        for i in range(n-2, -1, -1):
            max_ = 0
            
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    max_ = max(max_, dp[j])
            
            dp[i] = max_ + 1
            total_max = max(total_max, dp[i])
        
        return total_max