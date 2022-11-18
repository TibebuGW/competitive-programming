class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = 1
        
        main_dp = [-1]*(n+1)
        
        for i in range(n-1, -1, -1):
            min_ = float(inf)
            for j in range(i, n):
                if dp[i][j]:
                    min_ = min(min_, main_dp[j+1]+1)
            main_dp[i] = min_
        
        return main_dp[i]