class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        @lru_cache(None)
        def dp(i = m - 1, j = n - 1):
            
            if i == -1:
                if j == -1:
                    return True
                if p[j] == "*":
                    return dp(i, j - 2)
                else:
                    return False
            if j == -1:
                return False
            
            if p[j] != "*":
                if s[i] == p[j] or p[j] == ".":
                    return dp(i - 1, j - 1)
                return False
            
            
            if s[i] == p[j - 1] or p[j - 1] == ".":
                return dp(i - 1, j) or dp(i, j - 2)
            
            return dp(i, j - 2)
        
        return dp()