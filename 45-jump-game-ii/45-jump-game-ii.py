class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {len(nums)-1: 0}
        last = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= last:
                min_ = float('inf')
                for j in range(i+nums[i], i, -1):
                    if j < len(nums) and dp[j] != -1:
                        min_ = min(min_, dp[j])
                dp[i] = min_+1
                last = i
            else:
                dp[i] = -1
        return dp[0]
            
            