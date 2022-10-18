class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        in_range = lambda row, col: 0 <= row < rows and 0 <= col < cols
        ans = []
        row = rStart
        col = cStart
        count = 1
        while len(ans) < rows*cols:
            for i in range(col, col+count):
                if in_range(row, i):
                    ans.append([row, i])
            
            col += count
            
            for i in range(row, row+count):
                if in_range(i, col):
                    ans.append([i, col])
            
            row += count
            count += 1
            
            for i in range(col, col-count, -1):
                if in_range(row, i):
                    ans.append([row, i])
            
            col -= count
            
            for i in range(row, row-count, -1):
                if in_range(i, col):
                    ans.append([i, col])
            
            row -= count
            count += 1
        
        return ans