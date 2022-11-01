class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        count = 0
        in_range = lambda row, col: 0<=row<n and 0<=col<m
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def dfs(row, col):
            for x, y in directions:
                if in_range(row+x, col+y) and board[row+x][col+y] == "X":
                    board[row+x][col+y] = "."
                    dfs(row+x, col+y)
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    board[i][j] = "."
                    dfs(i, j)
                    count += 1
        return count