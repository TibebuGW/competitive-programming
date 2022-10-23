class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        ans = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] not in visited:
                ans = max(ans, r-l+1)
                visited.add(s[r])
            else:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1        
        return ans