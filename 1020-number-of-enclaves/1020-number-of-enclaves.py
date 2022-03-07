class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        n = len(board)
        m = len(board[0])
        count = 0
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        in_bound = lambda row, col: 0 <= row < n and 0 <= col < m
        
        def dfs(x,y):
            board[x][y] = "Y"
            for i in range(4):
                tempx = x+directions[i][0]
                tempy = y+directions[i][1]
                if in_bound(tempx, tempy) and board[tempx][tempy] == 1:
                    dfs(tempx, tempy)
            
        
        for i in range(n):
            if board[i][0] == 1:
                dfs(i,0)
            if board[i][m-1] == 1:
                dfs(i,m-1)
                
        for i in range(m):
            if board[0][i] == 1:
                dfs(0,i)
            if board[n-1][i] == 1:
                dfs(n-1,i)
            
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    count += 1
                    
                    
        return count
                    
                    
                    