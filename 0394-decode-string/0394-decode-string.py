class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        i = 0
        
        def rec():
            nonlocal i
            
            digits = []
            while s[i].isdigit():
                digits.append(s[i])
                i += 1
            
            num = int("".join(digits))
            
            i += 1
            chars = []
            while s[i] != "]":
                if s[i].isalpha():
                    chars.append(s[i])
                elif s[i].isdigit():
                    chars.append(rec())
                i += 1
            
            return num * "".join(chars)
        
        while i < len(s):
            char = s[i]
            if char.isalpha():
                ans.append(char)
            elif char.isdigit():
                ans.append(rec())
            i += 1
        
        return "".join(ans)
                