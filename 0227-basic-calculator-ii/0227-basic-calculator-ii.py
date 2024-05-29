class Solution:
    def calculate(self, s: str) -> int:
        operator_stack = deque([])
        digit_stack = deque([])
        if s[0] == "-":
            digit_stack.append(0)
        
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
                digit_stack.append(int("".join(temp)))
                if operator_stack and (operator_stack[-1] == "*" or operator_stack[-1] == "/"):
                    num1 = digit_stack.pop()
                    num2 = digit_stack.pop()
                    if operator_stack[-1] == "*":
                        digit_stack.append(num1 * num2)
                    else:
                        digit_stack.append(num2 // num1)
                    operator_stack.pop()
            else:
                operator_stack.append(s[i])
            
            i += 1
        
        while operator_stack:
            num1 = digit_stack.popleft()
            num2 = digit_stack.popleft()
            if operator_stack[0] == "+":
                digit_stack.appendleft(num1 + num2)
            else:
                digit_stack.appendleft(num1 - num2)
            operator_stack.popleft()
        
        assert(len(digit_stack) == 1)
        
        return digit_stack[0]