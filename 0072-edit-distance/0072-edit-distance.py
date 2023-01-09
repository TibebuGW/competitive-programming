class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        
        @lru_cache(None)
        def dp(idx1 = m, idx2 = n):
            
            if idx1 == 0:
                return idx2
            
            if idx2 == 0:
                return idx1
            
            if idx2 <= 0:
                return max(idx1, 0)
            
            if word1[idx1 - 1] == word2[idx2 - 1]:
                return dp(idx1 - 1, idx2 - 1)
            
            insertion = dp(idx1, idx2 - 1)
            deletion = dp(idx1 - 1, idx2)
            replacement = dp(idx1 - 1, idx2 - 1)
            
            return min(insertion, deletion, replacement) + 1
        
        return dp()