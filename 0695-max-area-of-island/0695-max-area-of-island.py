class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        
        def dfs(i, j):
            cur_ = 1
            grid[i][j] = 2
            
            for row, col in directions:
                new_row = i + row
                new_col = j + col
                if in_range(new_row, new_col) and grid[new_row][new_col] == 1:
                    cur_ += dfs(new_row, new_col)
            
            return cur_
        
        max_ = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_ = max(max_, dfs(i, j))
        
        return max_