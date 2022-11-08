class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        min_ = float('inf')
        queue = deque([(0, 0, k)])
        last = (n-1, m-1)
        level = 0
        in_range = lambda row, col: 0<=row<n and 0<=col<m
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set((0, 0, k))
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if (node[0], node[1]) == last:
                    return level
                else:
                    for row_move, col_move in directions:
                        new_row = node[0] + row_move
                        new_col = node[1] + col_move
                        if in_range(new_row, new_col):
                            obstacle_so_far = node[2]-grid[new_row][new_col]
                            if (new_row, new_col, obstacle_so_far) not in visited and obstacle_so_far >= 0:
                                visited.add((new_row, new_col, obstacle_so_far))
                                queue.append((new_row, new_col, obstacle_so_far))
            level += 1
        
        return min_ if min_ != float('inf') else -1