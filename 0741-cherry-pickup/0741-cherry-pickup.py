class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        in_range = lambda row, col: 0 <= row < n and 0 <= col < n
        
        @lru_cache(None)
        def dp(r1 = 0, c1 = 0, c2 = 0):
            r2 = r1 + c1 - c2
            if not in_range(r1, c1) or not in_range(r2, c2) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if r1 == n-1 and c1 == n-1 or r2 == n-1 and c2 == n-1:
                return grid[-1][-1]
            
            cur_cherries = 0
            if r1 == r2 and c1 == c2:
                cur_cherries = grid[r1][c1]
            else:
                cur_cherries = grid[r1][c1] + grid[r2][c2]
            
            next_cherries = float('-inf')
            
            case1 = dp(r1 + 1, c1, c2)
            case2 = dp(r1, c1 + 1, c2 + 1)
            case3 = dp(r1 + 1, c1, c2 + 1)
            case4 = dp(r1, c1 + 1, c2)
            
            next_cherries = max(case1, case2, case3, case4)
            
            return cur_cherries + next_cherries
    
        return max(0, dp())