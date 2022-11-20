class Solution:
    def applyOperation(self, num1, num2, op):
        if op == "+": return num1 + num2
        else: return num1 - num2
        
    def calculate(self, s: str) -> int:
        values = []
        ops = []
        expression = []
        for char in s:
            if char != " ":
                expression.append(char)
        
        i = 0
        while i < len(expression):
            char = expression[i]
            if char == "+" or char == "-":
                if char == "-" and (i == 0 or expression[i-1] == "("):
                    values.append(0)
                while ops and (ops[-1] == "+" or ops[-1] == "-"):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.applyOperation(val1, val2, op))
                ops.append(char)
            elif char.isdigit():
                val = int(char)
                i += 1
                while i < len(expression) and expression[i].isdigit():
                    val = (val*10) + int(expression[i])
                    i += 1
                i -= 1
                values.append(val)
            elif char == "(":
                ops.append(char)
            else:
                
                while ops and ops[-1] != "(":
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.applyOperation(val1, val2, op))
                
                ops.pop()
            
            i += 1
        
        while ops:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(self.applyOperation(val1, val2, op))
        
        return values[0]