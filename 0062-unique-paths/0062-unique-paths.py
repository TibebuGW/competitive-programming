class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        in_bound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_bound(i, j):
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            return right + down
        
        return dp()