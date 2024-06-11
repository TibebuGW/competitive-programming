class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        @lru_cache(None)
        def dp(index = 0, limit = k):
            if limit == 1:
                return prefix[-1] - prefix[index]
            
            min_ = float('inf')
            for j in range(index, len(nums)):
                cur_sum = prefix[j + 1] - prefix[index]
                min_ = min(min_, max(cur_sum, dp(j + 1, limit - 1)))
            
            return min_
        
        return dp()