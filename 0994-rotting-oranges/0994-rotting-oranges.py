class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        queue = deque([])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        level = 0
        while queue:
            length = len(queue)
            while length:
                cur_x, cur_y = queue.popleft()
                for dx, dy in directions:
                    new_x = cur_x + dx
                    new_y = cur_y + dy
                    
                    if in_range(new_x, new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                length -= 1
            level += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return max(0, level - 1)