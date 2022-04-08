class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        in_bound = lambda row, col: 0 <= row < m and 0 <= col < n
        dp = [[0]*n]*m
        # print(dp)
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                    
        
        
        return dp[-1][-1]
        