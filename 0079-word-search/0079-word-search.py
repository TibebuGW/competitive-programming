class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        WORD_KEY = '$'
        
        trie = {}
        node = trie
        for letter in word:
            node = node.setdefault(letter, {})
        node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)
            
            board[row][col] = '#'
            
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            board[row][col] = letter
        
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return len(matchedWords) == 1