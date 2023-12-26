class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        dp[-1] = 0
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            min_length = float('inf')
            for j in range(i + 1, min(n, nums[i] + i + 1)):
                min_length = min(min_length, dp[j])
            
            dp[i] = min_length + 1
        
        return dp[0]