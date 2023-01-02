class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        
        
        def dfs(i, j, tag):
            
            for row_move, col_move in directions:
                new_row = i + row_move
                new_col = j + col_move
                
                if in_range(new_row, new_col) and heights[i][j] <= heights[new_row][new_col]:
                    if tag == "p":
                        if (new_row, new_col) not in pacific_visited:
                            pacific_visited.add((new_row, new_col))
                            dfs(new_row, new_col, tag)
                    else:
                        if (new_row, new_col) not in atlantic_visited:
                            atlantic_visited.add((new_row, new_col))
                            dfs(new_row, new_col, tag)
        
        for j in range(n):
            pacific_visited.add((0, j))
            dfs(0, j, "p")
        
        for i in range(m):
            pacific_visited.add((i, 0))
            dfs(i, 0, "p")
        
        for j in range(n):
            atlantic_visited.add((m - 1, j))
            dfs(m - 1, j, "a")
        
        for i in range(m):
            atlantic_visited.add((i, n - 1))
            dfs(i, n - 1, "a")
        
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    ans.append([i, j])
        
        return ans