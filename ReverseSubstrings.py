class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        toReturn = ""
        temp = ""
        n = 0
        for i in range(0, len(s), 1):
            n = 0
            if s[i] != ")":
                stack.append(s[i])
            else:
                j = len(stack)-1
                while stack[j] != "(":
                    n+=1
                    j-=1
                temp = stack[len(stack)-n:len(stack)][::-1]
                stack = stack[0:len(stack)-1-n]
                stack.extend(temp)
            
            print(stack)
                    
        
        for i in range(0, len(stack), 1):
            if stack[i] != "(" or stack[i] != ")":
                toReturn += str(stack[i])
        
            
                
        return toReturn
