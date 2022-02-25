class Solution:
    def negativeCounter(self, arr):
        left = 0 
        right = len(arr)-1
        best = len(arr)
        while left <= right:
            mid = (left+right)//2
            if arr[mid] < 0:
                best = mid
                right = mid-1
            else:
                left = mid+1
        
            
        print(best)
        return len(arr)-best
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            count += self.negativeCounter(grid[i])
        
        return count
