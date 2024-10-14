class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        
        @lru_cache(None)
        def dp(i = 1, j = len(nums)):
            if i > j:
                return 0
            
            ans = float('-inf')
            for k in range(i, j + 1):
                cur_cost = arr[i - 1] * arr[k] * arr[j + 1] + dp(i, k - 1) + dp(k + 1, j)
                ans = max(ans, cur_cost)
            
            return ans
        
        return dp()