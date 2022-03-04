class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        Os = []
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        in_bound = lambda row, col: 0 <= row < n and 0 <= col < m
        
        def dfs(x,y):
            board[x][y] = "Y"
            for i in range(4):
                tempx = x+directions[i][0]
                tempy = y+directions[i][1]
                if in_bound(tempx, tempy) and board[tempx][tempy] == "O":
                    dfs(tempx, tempy)
            
        
        for i in range(n):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][m-1] == "O":
                dfs(i,m-1)
                
        for i in range(m):
            if board[0][i] == "O":
                dfs(0,i)
            if board[n-1][i] == "O":
                dfs(n-1,i)
                
            # for j in range(m):
            #     if board[i][j] == "O" and (i == 0 or j == 0 or i == n-1 or j == m-1):
            #         # print(board[i][j])
            #         dfs(i,j)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
                
                    
        # print(Os)

        # result = [(1,1),(2,3)]
        # print((2,3) in result)