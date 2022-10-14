class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = nums[0]
        min_ = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            max__ = max(max_*nums[i], min_*nums[i], nums[i])
            min__ = min(min_*nums[i], max_*nums[i], nums[i])
            max_, min_ = max__, min__
            ans = max(ans, max_)
        
        return ans