class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = [0]
        
        @lru_cache(None)
        def dp(index = 0, total = 0):
            if index == len(nums):
                return int(total == target)
            
            return dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index])
        
        return dp()