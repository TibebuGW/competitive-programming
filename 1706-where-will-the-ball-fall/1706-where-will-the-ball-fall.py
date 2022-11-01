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
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]
            if row == len(grid):
                return col

            # print(row, col)
            if self.stuck(grid, row, col):
                return -1
            else:
                next_col = col+1 if grid[row][col]==1 else col-1
                memo[row][col] = dfs(row+1, next_col)
                return memo[row][col]
        
        for i in range(n):
            # print(i)
            ans[i] = dfs(0, i)
            
        return ans
        
        