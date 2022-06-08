class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ds = Counter(s)
        dt = Counter(t)
        
        for char in s:
            if ds[char] != dt[char]:
                return False
            
        return True