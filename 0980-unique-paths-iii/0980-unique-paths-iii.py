class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        start_row = 0
        start_col = 0
        zeros = 0
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        in_bound = lambda row, col: 0<=row<n and 0<=col<m
        ans = [0]
        
        def dfs(row, col, count):
            
            if grid[row][col] == 2:
                if count == zeros:
                    ans[0] += 1
                return
            else:
                value = grid[row][col]
                grid[row][col] = -1
                for row_move, col_move in directions:
                    new_row = row + row_move
                    new_col = col + col_move
                    
                    if in_bound(new_row, new_col) and grid[new_row][new_col] != -1:
                        if grid[new_row][new_col] == 0:
                            dfs(new_row, new_col, count+1)
                        else:
                            dfs(new_row, new_col, count)
                grid[row][col] = value
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zeros += 1
                elif grid[i][j] == 1:
                    start_row = i
                    start_col = j
    
        
        dfs(start_row, start_col, 0)
        return ans[0]