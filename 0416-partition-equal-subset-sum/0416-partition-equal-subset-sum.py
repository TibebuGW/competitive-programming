class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total%2 == 1:
            return False
        half = total//2
        
        @lru_cache(None)
        def dp(target, index):
            if target == 0:
                return True
            if index == N:
                return False
            
            return dp(target-nums[index], index+1) or dp(target, index+1)
        
        
        if dp(half, 0):
            return True
        
        return False