class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        count = 1
        while top <= bottom:
            
            for i in range(left, right+1):
                matrix[top][i] = count
                count += 1
            top += 1
            
            for i in range(top, bottom+1):
                matrix[i][right] = count
                count += 1
            right -= 1
            
            for i in range(right, left-1, -1):
                matrix[bottom][i] = count
                count += 1
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
            
        return matrix