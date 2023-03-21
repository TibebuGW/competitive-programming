class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def options(l = 0, r = len(nums) - 1) -> int:
        
            if l > r:
                return 0
            if l == r:
                return nums[l]

            options1 = nums[l] + min(options(l+1, r-1), options(l+2, r))
            options2 = nums[r] + min(options(l, r-2), options(l+1, r-1))

            return max(options1, options2)
        
        total = sum(nums)
        p1 = options(0, len(nums)-1)
        return p1 >= total - p1