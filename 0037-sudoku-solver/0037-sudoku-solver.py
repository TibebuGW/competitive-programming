class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        box_index_calculator = lambda i, j: ((i//3)*3)+(j//3)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    box_index = box_index_calculator(i, j)
                    row[i].add(num)
                    col[j].add(num)
                    boxes[box_index].add(num)
        
        flag = [False]
        def backTrack(i, j):
            if i == 9:
                flag[0] = True
                return
            new_i = i + (j//8)
            new_j = (j+1)%9
            if board[i][j] != ".":
                backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_index = box_index_calculator(i, j)
                    if num not in row[i] and num not in col[j] and num not in boxes[box_index]:
                        board[i][j] = str(num)
                        row[i].add(num)
                        col[j].add(num)
                        boxes[box_index].add(num)
                        
                        backTrack(new_i, new_j)
                        
                        if not flag[0]:
                            board[i][j] = "."
                            row[i].remove(num)
                            col[j].remove(num)
                            boxes[box_index].remove(num)
                        else:
                            break
            
        backTrack(0,0)
                        