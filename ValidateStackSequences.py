class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped.reverse()
        for i in range(0, len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
                
        print(stack)
        if len(stack) != 0:
            return False
        else: 
            return True
