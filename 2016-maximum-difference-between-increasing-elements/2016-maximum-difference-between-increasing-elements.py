class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        max_so_far = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= max_so_far:
                max_so_far = nums[i]
            else:
                max_diff = max(max_diff, max_so_far - nums[i])
        
        return max_diff