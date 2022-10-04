class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [-1]*len(arr)
        right = [len(arr)]*len(arr)
        
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                right[stack.pop()] = i
            stack.append(i)
        
        stack = []
        
        for i in range(len(arr)-1, -1 ,-1):
            while stack and arr[i] < arr[stack[-1]]:
                left[stack.pop()] = i
            stack.append(i)
        
        total = 0
        
        for i in range(len(arr)):
            left_elements = i-left[i]-1
            right_elements = right[i]-i-1
            total += arr[i]*(left_elements+right_elements+(right_elements*left_elements+1))
        
        return total%1000000007