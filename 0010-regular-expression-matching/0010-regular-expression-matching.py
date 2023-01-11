class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        @lru_cache(None)
        def dp(i = m - 1, j = n - 1):
            
            if i == -1:
                if j == -1:
                    return True
                count = 0
                for idx in range(j + 1):
                    if p[idx] == "*":
                        count += 1
                return int(math.ceil((j+1)/2)) == count
            
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