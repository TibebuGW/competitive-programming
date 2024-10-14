class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_range(i, j) or obstacleGrid[i][j] == 1:
                return 0
            if i == n - 1 and j == m - 1:
                return 1
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            return right + down
        
        return dp()