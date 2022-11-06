class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all words into the prefix tree 
        root = {}
        for word in words:
            cur = root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur["WORD"] = word
        
        # declare necessary stuff
        ans = []
        n = len(board)
        m = len(board[0])
        in_bound = lambda row, col: 0<=row<n and 0<=col<m
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = set()
        
        # starting from a letter on the board, see if you can form a word from the word list
        def dfs(row, col, node):
            letter = board[row][col]
            curNode = node[letter]
            word_match = curNode.pop("WORD", False)
            if word_match:
                ans.append(word_match)
            
            board[row][col] = "#"
            for row_move, col_move in [[-1,0],[1,0],[0,1],[0,-1]]:
                new_row = row+row_move
                new_col = col+col_move
                
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue
                if not board[new_row][new_col] in curNode:
                    continue
                    
                cur_char = board[new_row][new_col]
                dfs(new_row, new_col, curNode)
            if not curNode:
                node.pop(letter)
                    
            board[row][col] = letter
            return
        
        # if a letter on the board is a start of a word, do dfs on it
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    dfs(i, j, root)
        return ans