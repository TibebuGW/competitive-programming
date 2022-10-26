class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        arr = [1, 1]
        
        while arr[-1] <= k:
            arr.append(arr[-1]+arr[-2])
        
        arr.pop()
        
        count = 0
        total = 0
        
        for pointer in range(len(arr)-1, -1, -1):
            if arr[pointer] + total < k:
                total += arr[pointer]
                count += 1
            elif arr[pointer] + total == k:
                count += 1
                return count
