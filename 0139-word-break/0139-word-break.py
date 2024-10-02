class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        @lru_cache(None)
        def dp(index = 0):
            if index == len(s):
                return True
            
            for i in range(index, len(s)):
                if s[index:i + 1] in wordSet and dp(i + 1):
                    return True
                
        return dp()