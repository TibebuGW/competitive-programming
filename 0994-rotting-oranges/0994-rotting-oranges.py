class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        in_range = lambda i, j: 0 <= i < n and 0 <= j < m
        level = 0
        
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            length = len(queue)
            level += 1
            
            for _ in range(length):
                i, j = queue.popleft()
                for row, col in directions:
                    new_row = row + i
                    new_col = col + j
                    if in_range(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
            
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return max(0, level - 1)