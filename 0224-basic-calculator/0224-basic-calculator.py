class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                temp = []
                while i < len(s) and s[i].isdigit():
                    temp.append(s[i])
                    i += 1
                i -= 1
                stack.append(int("".join(temp)))
            else:
                if s[i] == ")":
                    digit_stack = []
                    operator_stack = []
                    while stack and stack[-1] != "(":
                        if stack[-1] == "+" or stack[-1] == "-":
                            operator_stack.append(stack.pop())
                        else:
                            digit_stack.append(stack.pop())
                    stack.pop()
                    
                    if len(digit_stack) == len(operator_stack):
                        digit_stack.append(0)
                    while operator_stack:
                        num1 = digit_stack.pop()
                        num2 = digit_stack.pop()
                        if operator_stack[-1] == "+":
                            digit_stack.append(num1 + num2)
                        else:
                            digit_stack.append(num1 - num2)
                        operator_stack.pop()
                    stack.append(digit_stack[0])
                    
                else:
                    stack.append(s[i])
        
            i += 1
        
        digit_stack = []
        operator_stack = []
        while stack:
            if stack[-1] == "+" or stack[-1] == "-":
                operator_stack.append(stack.pop())
            else:
                digit_stack.append(stack.pop())
        
        if len(digit_stack) == len(operator_stack):
            digit_stack.append(0)
                
        while operator_stack:
            if operator_stack[-1] == "+":
                digit_stack.append(digit_stack.pop() + digit_stack.pop())
            else:
                digit_stack.append(digit_stack.pop() - digit_stack.pop())
            operator_stack.pop()
        
        return digit_stack[0]