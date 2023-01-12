class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        
        @lru_cache(None)
        def dp(i = n - 1, j = m - 1):
            
            if i == -1:
                if j == -1:
                    return True
                if p[j] == "*":
                    return dp(i, j - 1)
                return False
            
            if j == -1:
                return False
            
            if p[j] != "*":
                if s[i] == p[j] or p[j] == "?":
                    return dp(i - 1, j - 1)
                return False
            
            return dp(i - 1, j) or dp(i, j - 1)
        
        return dp()