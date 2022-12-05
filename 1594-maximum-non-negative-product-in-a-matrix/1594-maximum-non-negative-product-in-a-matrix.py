class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        MOD = (10**9) + 7
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_range(i, j):
                return []
            
            if i == m - 1 and j == n - 1:
                return [grid[i][j], grid[i][j]]
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            cur_max = -(4**15)
            cur_min = 4**15
            for val in right:
                cur_max = max(cur_max, val*grid[i][j])
                cur_min = min(cur_min, val*grid[i][j])
            
            for val in down:
                cur_max = max(cur_max, val*grid[i][j])
                cur_min = min(cur_min, val*grid[i][j])
                
            return [cur_max, cur_min]
        
        max_ans, min_ans =  dp()
        if max_ans < 0:
            return -1
        else:
            return max_ans%MOD