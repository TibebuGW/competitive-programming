class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        MOD = 10**9 + 7
        ans = 0
        
        @lru_cache(None)
        def dp(i, j):
            max_ = 1
            
            for row_move, col_move in directions:
                new_row = i + row_move
                new_col = j + col_move
                if in_range(new_row, new_col) and grid[new_row][new_col] > grid[i][j]:
                    max_ += dp(new_row, new_col)
            
            return max_
        
        for i in range(m):
            for j in range(n):
                ans += dp(i, j)
        
        return ans % MOD