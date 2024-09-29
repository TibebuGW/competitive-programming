class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        
        while l < r:
            
            for i in range(r - l):
                t, b = l, r
                
                carry = matrix[t + i][r]
                matrix[t + i][r] = matrix[t][l + i]
                
                temp = matrix[b][r - i]
                matrix[b][r - i] = carry
                carry = temp
                
                temp = matrix[b - i][l]
                matrix[b - i][l] = carry
                carry = temp
                
                matrix[t][l + i] = carry
            
            l += 1
            r -= 1