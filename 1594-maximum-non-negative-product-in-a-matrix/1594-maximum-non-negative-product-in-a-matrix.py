class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_range(i, j):
                return []
            
            if i == n - 1 and j == m - 1:
                return [grid[i][j], grid[i][j]]
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            max_ = -(10**6)
            min_ = 10**6
            for val in right:
                max_ = max(max_, val*grid[i][j])
                min_ = min(min_, val*grid[i][j])
            
            for val in down:
                max_ = max(max_, val*grid[i][j])
                min_ = min(min_, val*grid[i][j])
                
            return [min_, max_]
            
        ans = dp()[1]
        if ans < 0:
            return -1
        return ans % 1_000_000_007 