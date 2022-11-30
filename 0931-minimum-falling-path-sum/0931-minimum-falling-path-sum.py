class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        in_range = lambda row, col: 0 <= row < n and 0 <= col < n
        
        @lru_cache(None)
        def dp(r, c):
            if not in_range(r, c):
                return float('inf')
            
            if r == n - 1:
                return matrix[r][c]
            
            cur_score = matrix[r][c]
            
            next_score = float('inf')
            
            for move in [-1, 0, 1]:
                next_score = min(next_score, dp(r + 1, c + move))
            
            return cur_score + next_score
        
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp(0, i))
        
        return ans