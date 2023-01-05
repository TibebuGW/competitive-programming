class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        @lru_cache(None)
        def dp(idx1 = 0, idx2 = 0):
            if idx1 == n or idx2 == m:
                return 0
            
            if text1[idx1] == text2[idx2]:
                return 1 + dp(idx1 + 1, idx2 + 1)
            
            return max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))
        
        return dp()