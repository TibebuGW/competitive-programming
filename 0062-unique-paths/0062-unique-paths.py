class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        in_range = lambda x, y: 0 <= x < m and 0 <= y < n
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if i == m - 1 and j == n - 1:
                return 1
            
            if not in_range(i, j):
                return 0
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            return right + down
        
        return dp()