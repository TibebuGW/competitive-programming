class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        stack = []
        
        for index, value in enumerate(height):
            while stack and stack[-1][0] < value:
                last = stack.pop()
                min_ = min(value, stack[-1][0]) if stack else 0
                diff = index-stack[-1][1]-1 if stack else 0
                total += (min_-last[0])*diff if (min_ * diff)-last[0] > 0 else 0
            
            stack.append((value, index))
        
        return total