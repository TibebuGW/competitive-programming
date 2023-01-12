class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l = len(s3)
        m = len(s1)
        n = len(s2)
        
        @lru_cache(None)
        def dp(i = m - 1, j = n - 1, k = l - 1):
            
            if i == j == k == -1:
                return True
            
            if i == -1:
                if j > -1 and k > -1 and s2[j] == s3[k]:
                    return dp(i, j - 1, k - 1)
                return False
            
            if j == -1:
                if i > -1 and k > -1 and s1[i] == s3[k]:
                    return dp(i - 1, j, k - 1)
                return False
            
            if k == -1:
                return False
            
            if s1[i] == s2[j] == s3[k]:
                return dp(i - 1, j, k - 1) or dp(i, j - 1, k - 1)
            
            if s1[i] == s3[k]:
                return dp(i - 1, j, k - 1)
            
            if s2[j] == s3[k]:
                return dp(i, j - 1, k - 1)
            
            return False
        
        return dp()