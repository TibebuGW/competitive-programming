class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        div = [0 for _ in range(len(word))]
        prefix = 0
        
        for i in range(len(word)):
            prefix = (prefix * 10) + int(word[i])
            if prefix % m == 0:
                div[i] = 1
            prefix %= m
        return div