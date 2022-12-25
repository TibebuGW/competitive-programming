class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        first_row_flag = first_col_flag = False
        m = len(matrix)
        n = len(matrix[0])
        
        if matrix[0][0] == 0:
            first_row_flag = first_col_flag = True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_flag = True
                    elif j == 0:
                        first_col_flag = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if first_row_flag:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_flag:
            for i in range(m):
                matrix[i][0] = 0
        
        return