class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        best = -1
        while left <= right:
            mid = (left+right)//2
            
            if matrix[mid][0] > target:
                right = mid-1
                best = right
            elif matrix[mid][0] < target:
                left = mid+1
            else:
                return True
            
        arrindex = best
        # print(arrindex)
        
        left = 0
        right = len(matrix[arrindex])-1
        
        while left <= right:
            mid = (left+right)//2
            
            if matrix[arrindex][mid] > target:
                right = mid-1
            elif matrix[arrindex][mid] < target:
                left = mid+1
            else:
                return True
        
        return False