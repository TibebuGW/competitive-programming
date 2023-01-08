class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        
        @lru_cache(None)
        def dp(idx1 = n - 1, idx2 = n - 1):
            
            if idx1 == 0:
                for i in range(idx2 + 1):
                    if t[i] == s[idx1]:
                        return 1
                return 0
            
            if idx2 == 0:
                for i in range(idx1 + 1):
                    if s[i] == t[idx2]:
                        return 1
                return 0
            
            if s[idx1] == t[idx2]:
                return 1 + dp(idx1 - 1, idx2 - 1)
            
            return max(dp(idx1 - 1, idx2), dp(idx1, idx2 - 1))
            
        
        return n - dp()