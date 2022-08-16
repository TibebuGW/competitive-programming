from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        set_ = set()
        while i < len(s):
            if s[i] not in set_:
                j = i+1
                flag = True
                while j < len(s):
                    if s[j] == s[i]:
                        flag = False
                        break
                    j += 1

                set_.add(s[i])
                if flag:
                    return i
            i += 1
        
        return -1