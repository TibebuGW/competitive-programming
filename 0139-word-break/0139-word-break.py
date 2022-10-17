class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        @lru_cache(None)
        def solve(index):
            if index >= len(s):
                return True
            
            for i in range(index+1, len(s)+1):
                if s[index:i] in wordDict and solve(i):
                    return True
            
            return False
        
        return solve(0)