class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        half = n//2
        limiter = n - 1
        
        for i in range(half):
            for j in range(i, limiter):
                carry = matrix[i][j]
                first_alternator = j
                second_alternator = abs(n - 1 - j)
                
                temp = matrix[first_alternator][limiter]
                matrix[first_alternator][limiter] = carry
                carry = temp
                
                temp = matrix[limiter][second_alternator]
                matrix[limiter][second_alternator] = carry
                carry = temp
                
                temp = matrix[second_alternator][i]
                matrix[second_alternator][i] = carry
                carry = temp
                
                matrix[i][j] = carry
                
            limiter -= 1