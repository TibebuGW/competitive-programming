class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x = click[0]
        y = click[1]
        m = len(board)
        n = len(board[0])
        in_bound = lambda row, col: 0<=row<m and 0<=col<n
        d = [[-1,0], [1,0], [0,-1], [0,1], [1,1], [1,-1], [-1,1], [-1,-1]]
        
        def dfs(x,y):
            count = 0
            for i in range(8):
                tempx = x+d[i][0]
                tempy = y+d[i][1]
                if in_bound(tempx, tempy) and board[tempx][tempy] == "M":
                    # print(tempx,tempy)
                    count += 1
            # print(count)
            if count == 0:
                board[x][y] = "B"
                for i in range(8):
                    tempx = x+d[i][0]
                    tempy = y+d[i][1]
                    if in_bound(tempx, tempy) and board[tempx][tempy] == "E":
                        # print(tempx,tempy)
                        dfs(tempx, tempy)
            else:
                board[x][y] = str(count)
                
            
        
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        else:
            dfs(x,y)
            return board
            