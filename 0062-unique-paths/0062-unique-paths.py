class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        
        @lru_cache(None)
        def dp(i, j):
            if i == m-1 and j == n-1:
                return 1
            
            if not in_range(i, j):
                return 0
            
            return dp(i+1, j) + dp(i, j+1)
        
        return dp(0, 0)