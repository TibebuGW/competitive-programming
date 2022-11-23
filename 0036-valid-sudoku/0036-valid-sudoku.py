class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                
                box_coordinates = (i//3, j//3)
                if board[i][j] in boxes[box_coordinates[0]*3 + box_coordinates[1]]:
                    return False
                else:
                    boxes[box_coordinates[0]*3 + box_coordinates[1]].add(board[i][j])
        
        return True