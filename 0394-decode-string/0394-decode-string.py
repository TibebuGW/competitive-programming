class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        
        while i < len(s):
            char = s[i]
            if char != "[" and char != "]":
                if char.isdigit():
                    digit_array = []
                    while s[i].isdigit():
                        digit_array.append(s[i])
                        i += 1
                    i -= 1
                    stack.append("".join(digit_array))
                else:
                    stack.append(char)
            elif char == "]":
                cur_string = []
                while not stack[-1].isdigit():
                    cur_string.append(stack.pop())
                
                multiplier = stack.pop()
                stack.append(int(multiplier) * "".join(cur_string[::-1]))
            
            i += 1
        
        return "".join(stack)