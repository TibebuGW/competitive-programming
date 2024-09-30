class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        half = total // 2
        
        @lru_cache(None)
        def dp(index = 0, total = 0):
            if index == len(nums):
                return total == half
            
            return dp(index + 1, total + nums[index]) or dp(index + 1, total)
        
        return dp()