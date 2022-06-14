class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = -1
        while len(popped) != 0 and count < len(pushed):
            if not stack or stack[-1] != popped[0]:
                if count == len(pushed)-1:
                    break
                stack.append(pushed[count+1])
                count += 1
            else:
                stack.pop()
                popped.pop(0)
            
        return len(stack) == 0