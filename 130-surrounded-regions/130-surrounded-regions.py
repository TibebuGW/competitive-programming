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
            Os.append((x,y))
            for i in range(4):
                tempx = x+directions[i][0]
                tempy = y+directions[i][1]
                if in_bound(tempx, tempy) and board[tempx][tempy] == "O" and (tempx,tempy) not in Os:
                    dfs(tempx, tempy)
            
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == n-1 or j == m-1):
                    # print(board[i][j])
                    dfs(i,j)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i,j) not in Os:
                    board[i][j] = "X"
                    
        # print(Os)

        # result = [(1,1),(2,3)]
        # print((2,3) in result)