class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(index = 0):
            if index == len(nums) - 1:
                return 1
            
            max_ = 0
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    max_ = max(max_, dp(i))
            
            return max_ + 1
        
        ans = 1
        for i in range(len(nums)):
            ans = max(ans, dp(i))
        
        return ans