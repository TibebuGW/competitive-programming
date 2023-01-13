class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(idx):
            
            
            max_ = 0
            for i in range(idx + 1, n):
                if nums[i] > nums[idx]:
                    max_ = max(max_, dp(i))
            return max_ + 1
        
        total_max = 1
        for i in range(n-1, -1, -1):
            total_max = max(total_max, dp(i))
        
        return total_max