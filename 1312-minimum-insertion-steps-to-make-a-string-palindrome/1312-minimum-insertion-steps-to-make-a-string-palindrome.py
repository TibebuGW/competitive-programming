class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def dp(l = 0, r = n - 1):
            
            if l >= r:
                return 0
            
            if s[l] == s[r]:
                return dp(l + 1, r - 1)
            
            return 1 + min(dp(l + 1, r), dp(l, r - 1))
        
        return dp()