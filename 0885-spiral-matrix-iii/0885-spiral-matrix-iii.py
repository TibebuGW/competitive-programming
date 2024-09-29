class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        in_range = lambda x, y: 0 <= x < rows and 0 <= y < cols
        moves = 1
        r, c = rStart, cStart
        i = 0
        
        while len(res) < rows * cols:
            
            for _ in range(2):
                
                dr, dc = directions[i]
                for _ in range(moves):
                    
                    if in_range(r, c):
                        res.append([r, c])
                    r, c = r + dr, c + dc
                
                i = (i + 1) % 4
            
            moves += 1
        
        return res