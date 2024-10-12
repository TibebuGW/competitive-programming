class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        ans = [-1]
        
        
        @lru_cache(None)
        def dp(i = 0, j = 0, total = 1):
            if not in_range(i, j):
                return
            
            if i == n - 1 and j == m - 1:
                ans[0] = max(ans[0], total * grid[i][j])
                return
            
            right = dp(i, j + 1, total * grid[i][j])
            down = dp(i + 1, j, total * grid[i][j])
            
        
        dp()
        return ans[0] % 1_000_000_007 if ans[0] != -1 else -1