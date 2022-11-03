class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        same = defaultdict(int)
        different = defaultdict(int)
        ans = 0
        for word in words:
            if word[0] == word[1]:
                if word in same:
                    ans += 4
                    del same[word]
                else:
                    same[word] = 1
            else:
                if different[word[::-1]]:
                    ans += 4
                    different[word[::-1]] -= 1
                else:
                    different[word] += 1
        
        if len(same):
            ans += 2
            
        return ans