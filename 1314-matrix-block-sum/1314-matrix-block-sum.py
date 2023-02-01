class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + mat[i][j]
        
        
        for i in range(m):
            for j in range(n):
                row_top = max(0, i - k)
                row_bottom = min(m - 1, i + k)
                col_left = max(0, j - k)
                col_right = min(n - 1, j + k)
                
                ans[i][j] = prefix[row_bottom + 1][col_right + 1] - prefix[row_top][col_right + 1] - prefix[row_bottom + 1][col_left] + prefix[row_top][col_left]
                
        
        return ans