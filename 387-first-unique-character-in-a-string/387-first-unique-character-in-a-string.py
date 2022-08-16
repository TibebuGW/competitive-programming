from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        ans = -1
        # print(d)
        for index in range(len(s)):
            if d[s[index]] == 1:
                ans = index
                break
        
        return ans