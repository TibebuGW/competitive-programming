class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        
        self.prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for index, row in enumerate(matrix):
            for i in range(n):
                self.prefix[index][i + 1] = self.prefix[index][i] + row[i]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = col1
        right = col2 + 1
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.prefix[i][right] - self.prefix[i][left]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)