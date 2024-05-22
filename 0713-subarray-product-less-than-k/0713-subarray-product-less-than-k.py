class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        total = 1
        
        l = 0
        for r in range(len(nums)):
            total *= nums[r]
            
            while l <= r and total >= k:
                total //= nums[l]
                l += 1
            
            ans += r - l + 1
        
        return ans