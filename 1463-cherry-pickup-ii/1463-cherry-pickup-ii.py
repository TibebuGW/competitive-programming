class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_range = lambda row, col: 0 <= row < n and 0 <= col < m
        
        @lru_cache(None)
        def dp(r1 = 0, c1 = 0, r2 = 0, c2 = m-1):
            if not in_range(r1, c1) or not in_range(r2, c2):
                return float('-inf')
            
            if r1 == n-1:
                return grid[r1][c1] + grid[r2][c2] if c1 != c2 else grid[r1][c1]
            
            cur_cherries = 0
            if c1 == c2:
                cur_cherries += grid[r1][c1]
            else:
                cur_cherries += grid[r1][c1] + grid[r2][c2]
            
            next_cherries = float('-inf')
            
            for move1 in [-1, 0, 1]:
                for move2 in [-1, 0, 1]:
                    value = dp(r1 + 1, c1 + move1, r2 + 1, c2 + move2)
                    next_cherries = max(next_cherries, value)
            
            return cur_cherries + next_cherries
        
        return dp()