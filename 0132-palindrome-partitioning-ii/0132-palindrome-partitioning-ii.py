class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
        
        @lru_cache(None)
        def solve(start = 0):
            if start == len(s):
                return 0
            
            ans = float('inf')
            
            for end in range(start, len(s)):
                if dp[start][end]:
                    ans = min(ans, solve(end+1))
            
            return ans+1
    
        return solve() - 1