class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def topdown(p1, p2):
            if p1 >= len(word1):
                return len(word2) - p2
            if p2 >= len(word2):
                return len(word1) - p1
            if word1[p1] == word2[p2]:
                return topdown(p1+1, p2+1)

            insertion = topdown(p1, p2+1)
            deletion = topdown(p1+1, p2)
            replace = topdown(p1+1, p2+1)
            return 1 + min(insertion, deletion, replace)
        return topdown(0, 0)