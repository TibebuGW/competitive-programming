class Solution:
    def stuck(self, grid, row, col):
        m = len(grid)
        n = len(grid[0])
        if col == 0 and grid[row][col] == -1 or col == n-1 and grid[row][col] == 1:
            return True
        if col > 0 and grid[row][col] == -1 and grid[row][col-1] == 1:
            return True
        if col < n-1 and grid[row][col] == 1 and grid[row][col+1] == -1:
            return True
        return False
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = [-1]*n
        for i in range(n):
            if self.stuck(grid, 0, i):
                continue
            else:
                next_col = i+1 if grid[0][i] == 1 else i-1
            for j in range(1, m):
                if self.stuck(grid, j, next_col):
                    next_col = -1
                    break
                else:
                    next_col = next_col+1 if grid[j][next_col] == 1 else next_col-1
            ans[i] = next_col
        
        return ans