class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split("/")
        stack = []
        for string in a:
            if string == "." or string == "":
                continue
            elif stack and string == "..":
                stack.pop()
            elif string != "..":
                stack.append(string)
            
            # print(stack)
        
        return "/" + "/".join(stack)