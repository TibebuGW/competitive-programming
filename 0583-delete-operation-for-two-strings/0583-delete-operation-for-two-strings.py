class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        @lru_cache(None)
        def dp(idx1 = m - 1, idx2 = n - 1):
            
            if idx1 == 0:
                for i in range(idx2 + 1):
                    if word1[idx1] == word2[i]:
                        return 1
                return 0
            
            if idx2 == 0:
                for i in range(idx1 + 1):
                    if word1[i] == word2[idx2]:
                        return 1
                return 0
            
            if word1[idx1] == word2[idx2]:
                return 1 + dp(idx1 - 1, idx2 - 1)
            
            return max(dp(idx1 - 1, idx2), dp(idx1, idx2 - 1))
        
        ans = dp()
        
        return m - ans + n - ans