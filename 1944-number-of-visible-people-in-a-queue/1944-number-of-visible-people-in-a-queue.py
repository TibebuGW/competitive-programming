class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        arr = [1]*(len(heights)-1) + [0]
        stack = []
        max_ = float('-inf')
        for i in range(len(heights)):
            
            while stack and heights[stack[-1]] < heights[i]:
                index = stack.pop()
                value = heights[index]
                if value > max_:
                    arr[index] += 1
                    max_ = value
            
            if stack and heights[stack[-1]] > max_:
                arr[stack[-1]] += 1
            
            stack.append(i)
            max_ = heights[i]
        
        return arr