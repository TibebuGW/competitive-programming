class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_range(i, j):
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return abs(min(0, dungeon[i][j])) + 1
            
            cur_needed = abs(min(0, dungeon[i][j])) + 1
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            next_needed = min(right, down)
            
            return max(cur_needed, max(0, next_needed - dungeon[i][j]))

        return dp()
