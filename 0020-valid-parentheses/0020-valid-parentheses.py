class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack