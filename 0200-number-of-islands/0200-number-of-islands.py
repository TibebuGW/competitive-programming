class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        ans = 0
        
        def marker(i, j):
            grid[i][j] = "0"
            for dx, dy in directions:
                new_x = dx + i
                new_y = dy + j
                if in_range(new_x, new_y) and grid[new_x][new_y] == "1":
                    marker(new_x, new_y)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    marker(i, j)
                    ans += 1
        
        return ans