class Solution:
    def decodeString(self, s: str) -> str:
        toReturn = ""
        stack = []
        
        for i in s:
            tempstr = ""
            tempnum = ""
            if i == "]":
                while stack and stack[-1] != "[":
                    tempstr += stack.pop()
                # print(tempstr)
                tempstr = tempstr[::-1]
                # print(tempstr)
                stack.pop()
                while stack and stack[-1].isdigit():
                    tempnum += stack.pop()
                tempnum = tempnum[::-1]
                
                for j in int(tempnum)*tempstr:
                    stack.append(j)
                # print(stack)
            else:
                stack.append(i)
        
        for i in range(len(stack)):
            toReturn += stack[i]
        
        return toReturn
