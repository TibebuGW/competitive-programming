class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = '+-/*'
        for i in range(0, len(tokens), 1):
            a = b = 0
            if tokens[i] not in ops:  
                stack.append(int(tokens[i]))
                
            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)+int(a))
                
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)-int(a))
                
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)*int(a))
                
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(int(b)/int(a)))
                
                
        
        return stack.pop()
                
            
