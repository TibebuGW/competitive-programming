class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        result = -1
        for i in range(len(haystack)):
            # print(haystack[i:i+n])
            if haystack[i:i+n] == needle:
                return i
        return result
                