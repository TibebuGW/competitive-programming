class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        
        @lru_cache(None)
        def dp(i = m - 1, j = n - 1):
            
            if i == 0:
                if j == 0 and s[i] == t[j]:
                    return 1
                return 0
            
            if j == 0:
                count = 0
                for idx in range(i + 1):
                    if s[idx] == t[j]:
                        count += 1
                return count
            
            if s[i] == t[j]:
                return dp(i - 1, j) + dp(i - 1, j - 1)
            
            return dp(i - 1, j)
        
        return dp()