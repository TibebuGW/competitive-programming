############ trial 2 ###########
from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                if not stack:
                    maxArea = max(maxArea, i*heights[h])
                else:
                    maxArea = max(maxArea, (i-stack[-1]-1)*heights[h])
            stack.append(i)
        
        while stack:
            h = stack.pop()
            if not stack:
                maxArea = max(maxArea, len(heights)*heights[h])
            else:
                maxArea = max(maxArea, (len(heights)-stack[-1]-1)*heights[h])
                
        return maxArea
############ trial 1 ###########
# from collections import deque
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = [-1]
#         maxArea = 0
#         heights.append(0)
#         for i in range(len(heights)):
#             while stack and heights[i] < heights[stack[-1]]:
#                 h = heights[stack.pop()]
#                 w = i-stack[-1]-1 
#                 maxArea = max(maxArea, h*w)
#             stack.append(i)
#         return maxArea
