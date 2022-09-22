class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {len(nums)-1: True}
        last = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= last:
                dp[i] = True
                last = i
            else:
                dp[i] = False
        
        return dp[0]
        