class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        boxCalculator = lambda i, j: ((i // 3) * 3) + (j // 3)
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    rows[i].add(int(cur))
                    cols[j].add(int(cur))
                    boxes[boxCalculator(i, j)].add(int(cur))
        
        
        def backtrack(i = 0, j = 0):
            if i == 9:
                return True
            
            next_i = i + ((j + 1) // 9)
            next_j = (j + 1) % 9
            if board[i][j] == ".":
                for num in range(1, 10):
                    if num not in rows[i] and num not in cols[j] and num not in boxes[boxCalculator(i, j)]:
                        board[i][j] = str(num)
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[boxCalculator(i, j)].add(num)
                        if backtrack(next_i, next_j):
                            return True
                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[boxCalculator(i, j)].remove(num)
                        board[i][j] = "."
                return False
            else:
                return backtrack(next_i, next_j)
            
        
        backtrack()