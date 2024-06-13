class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        ans = 0
        d = {0: -1}
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= (1 << vowels[s[i]])
            
            if mask in d:
                ans = max(ans, i - d[mask])
            else:
                d[mask] = i
        
        return ans