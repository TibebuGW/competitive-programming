class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # print("v" < "a")
        d = {}
        
        for i in range(len(s)):
            d[s[i]] = i
            
        # print(d)
        stack = []
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and d[stack[-1]] > i:
                seen.remove(stack.pop())
            seen.add(s[i])
            stack.append(s[i])
            
        return "".join(stack)