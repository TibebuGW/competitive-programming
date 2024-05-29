class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        left_to_right = [len(heights) - 1 for i in range(len(heights))]
        right_to_left = [0 for i in range(len(heights))]
        
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                left_to_right[stack.pop()] = i - 1
            stack.append(i)
        
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                right_to_left[stack.pop()] = i + 1
            stack.append(i)
            
        for i in range(len(heights)):
            width = left_to_right[i] - right_to_left[i] + 1
            ans = max(ans, width * heights[i])
        
        return ans