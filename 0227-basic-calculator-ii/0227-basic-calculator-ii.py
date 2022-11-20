class Solution:
    def applyOperation(self, num1, num2, op):
        if op == "+": return num1 + num2
        if op == "-": return num1 - num2
        if op == "/": return num1 // num2
        if op == "*": return num1 * num2
        
    def calculate(self, s: str) -> int:
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        values = []
        ops = []
        
        i = 0
        
        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
                continue
            elif char.isdigit():
                i += 1
                val = int(char)
                while i < len(s) and s[i].isdigit():
                    val = (val*10) + int(s[i])
                    i += 1
                i -= 1
                values.append(val)
            else:
                while ops and precedence[ops[-1]] >= precedence[char]:
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.applyOperation(val1, val2, op))
                ops.append(char)
            
            i += 1
        
        while ops:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(self.applyOperation(val1, val2, op))
        
        return values[0]