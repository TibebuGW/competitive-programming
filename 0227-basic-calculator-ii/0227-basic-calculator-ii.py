class Solution:
    def calculate(self, s: str) -> int:
        def applyOp(num1, num2, op):
            if op == "+": return num1 + num2
            elif op == "-": return num1 - num2
            elif op == "*": return num1 * num2
            else: return num1 // num2
        
        operator_stack = deque([])
        digit_stack = deque([])
        
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
                    digit_stack.append(applyOp(num2, num1, operator_stack.pop()))
            else:
                operator_stack.append(s[i])
            
            i += 1
        
        while operator_stack:
            num1 = digit_stack.popleft()
            num2 = digit_stack.popleft()
            digit_stack.appendleft(applyOp(num1, num2, operator_stack.popleft()))
        
        return digit_stack[0]