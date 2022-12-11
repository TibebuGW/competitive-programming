class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        left = [-1]*(len(arr))
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                left[index] = i
            stack.append(i)
            
        right = [len(arr)]*(len(arr))
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                right[index] = i
            stack.append(i)
        
        max_ans = 0
        for i in range(len(arr)):
            max_ans = max(max_ans, arr[i]*(right[i] - left[i] - 1))
        
        return max_ans