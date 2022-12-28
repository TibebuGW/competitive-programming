class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        total_zeros = 0
        ans = k
        
        l = 0
        for r in range(len(nums)):
            total_zeros += int(nums[r] == 0)
            
            if total_zeros <= k:
                ans = max(ans, r - l + 1)
            else:
                while total_zeros > k:
                    total_zeros -= int(nums[l] == 0)
                    l += 1
        
        return ans