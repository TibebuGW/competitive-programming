class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M = (10**9) + 7
        m = len(grid)
        n = len(grid[0])
        in_bound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        @lru_cache(None)
        def dp(i = 0, j = 0):
            if not in_bound(i, j):
                return {}
            
            if i == m - 1 and j == n - 1:
                return {grid[i][j]%k: 1}
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            cur = grid[i][j]%k
            d = defaultdict(int)
            
            for key, val in right.items():
                d[(key + cur)%k] += val
            
            for key, val in down.items():
                d[(key + cur)%k] += val
                
            return d
        
        ans = dp()
        if 0 in ans:
            return ans[0]%M
        return 0