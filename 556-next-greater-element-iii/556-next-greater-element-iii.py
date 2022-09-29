from struct import pack, error

class Solution:
    def test_32bit(self, n):
        try:
            pack("i", n)
        except error:
            return False
        return True
    
    def nextGreaterElement(self, n: int) -> int:
        stack = []
        
        while n > 0:
            num = n%10
            n //= 10
            # print(n, num)
            
            if not stack or stack[-1] <= num:
                stack.append(num)
            elif stack:
                stack.append(num)
                index = -1
                # print(stack)
                for i in range(len(stack)):
                    if stack[i] > num:
                        index = i
                        break
                
                stack[index], stack[-1] = stack[-1], stack[index]
                # print(stack)
                n = (n*10)+stack.pop()
                stack.sort()
                for ele in stack:
                    n = (n*10)+ele
                # print(n)
                return n if self.test_32bit(n) else -1
        # print(stack)
        # print(n)
        if n == 0:
            return -1