class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(i, j, index):
            if index == len(word) - 1:
                return True
            
            char = board[i][j]
            board[i][j] = "-"
            
            for dx, dy in directions:
                new_r, new_c = i + dx, j + dy
                if in_range(new_r, new_c) and board[new_r][new_c] == word[index + 1]:
                    if dfs(new_r, new_c, index + 1):
                        return True
            board[i][j] = char
            return False
        
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
                
        return False