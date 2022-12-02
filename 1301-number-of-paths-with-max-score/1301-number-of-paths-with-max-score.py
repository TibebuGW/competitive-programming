class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        in_range = lambda row, col: 0 <= row < n and 0 <= col < n
        
        @lru_cache(None)
        def dp(i = n - 1, j = n - 1):
            if not in_range(i, j) or board[i][j] == "X":
                return (float('-inf'), float('-inf'))
            
            if i == j == 0:
                return (0, 1)
            
            left_max, left_count = dp(i, j - 1)
            up_max, up_count = dp(i - 1, j)
            up_left_max, up_left_count = dp(i - 1, j - 1)
            
            count = 0
            max_ = max(left_max, up_max, up_left_max)
            
            if max_ == left_max:
                count += left_count
            
            if max_ == up_max:
                count += up_count
            
            if max_ == up_left_max:
                count += up_left_count
            
            cur_value = 0 if board[i][j] == "S" else int(board[i][j])
            return (max_ + cur_value, count)
        
        ans = dp()
        if ans[0] == float('-inf'):
            return [0, 0]
        else:
            return [ans[0], ans[1]%MOD]