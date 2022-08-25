class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        
        print(r)
        print(m)
        for char in ransomNote:
            if char not in m or not m[char]:
                return False
            m[char] -= 1
            
        
        return True