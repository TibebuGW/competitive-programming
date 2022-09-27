class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = {(0,0):0, (0,1): 1, (0,2):2, (1,0):3, (1,1):4, (1,2):5, (2,0):6, (2,1):7, (2,2):8}
        d = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    temp = subBoxes[(i//3, j//3)]
                    for row, col, subBox in d[board[i][j]]:
                        if row == i or col == j or temp == subBox:
                            return False
                    d[board[i][j]].append([i, j, temp])
        
        return True