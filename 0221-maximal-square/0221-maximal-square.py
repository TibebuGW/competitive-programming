class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        memo = {} # (r, c) -> max square length we can have from this position being the top left corner
        
        def dp(i = 0, j = 0):
            if not in_range(i, j):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = 0
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            diagonal = dp(i + 1, j + 1)
            if matrix[i][j] == "1":
                memo[(i, j)] = 1 + min(right, down, diagonal)
            
            return memo[(i, j)]
        
        dp()
        return max(memo.values()) ** 2