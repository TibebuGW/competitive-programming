class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = 0
        
        l = 0
        r = 0
        while r < len(nums):
            total += nums[r]
            
            while total >= target:
                ans = min(ans, r - l + 1)
                
                total -= nums[l]
                l += 1
            
            r += 1
        
        return ans if ans != float('inf') else 0