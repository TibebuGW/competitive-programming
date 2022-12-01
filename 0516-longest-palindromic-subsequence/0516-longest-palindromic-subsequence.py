class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
#         @lru_cache(None)
#         def dp(l = 0, r = n - 1):
#             if l == r:
#                 return 1
#             if l > r:
#                 return 0
            
#             if s[l] == s[r]:
#                 return dp(l + 1, r - 1) + 2
            
#             return max(dp(l, r - 1), dp(l + 1, r))
        
        # return dp()
    
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for l in range(n-1, -1, -1):
            for r in range(n):
                if l > r:
                    continue
                elif l == r:
                    dp[l][r] = 1
                else:
                    if s[l] == s[r]:
                        dp[l][r] = dp[l+1][r-1] + 2
                    else:
                        dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        
        return dp[0][-1]