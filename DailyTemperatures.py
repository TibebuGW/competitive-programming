class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        n = len(temperatures)-1
        stack = [n]
        
        for i in range(len(temperatures)-2, -1, -1):
            
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
                
            stack.append(i)
            
            if len(stack) == 1:
                result[i] = 0
            else:
                result[i] = stack[-2] - stack[-1]
                
                
        return result
            
