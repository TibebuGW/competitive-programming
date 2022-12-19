class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        
        @lru_cache(None)
        def dp(i, j):
            
            max_ = 0
            
            for dr, dy in directions:
                r, c = dr + i, dy + j
                if in_range(r, c) and matrix[r][c] > matrix[i][j]:
                    max_ = max(max_, dp(r, c))
            
            return max_ + 1
        
        maximum = 1
        for i in range(m):
            for j in range(n):
                maximum = max(maximum, dp(i, j))
        
        return maximum