class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        
        def dfs(i, j):
            board[i][j] = "Y"
            
            for row, col in directions:
                new_row = i + row
                new_col = j + col
                if in_range(new_row, new_col) and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and board[i][j] == "O":
                    dfs(i, j)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "Y":
                    board[i][j] = "O"
        