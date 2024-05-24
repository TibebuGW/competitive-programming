class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def isInteger(s):
            try:
                int(s)
                return True
            except:
                return False
        
        for char in tokens:
            if isInteger(char):
                stack.append(int(char))
            else:
                if char == "+":
                    stack.append(stack.pop() + stack.pop())
                elif char == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif char == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    ans = num2 / num1
                    if (ans < 0):
                        stack.append(math.ceil(ans))
                    else:
                        stack.append(math.floor(ans))
        return stack[0]