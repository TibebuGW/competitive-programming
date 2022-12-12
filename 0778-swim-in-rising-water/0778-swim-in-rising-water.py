class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # the grid is basically an undirected graph where the weight of an edge is the max of the two nodes it connects
        n = len(grid)
        minimum_time = defaultdict(lambda: float('inf'))
        minimum_time[(0,0)] = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        in_range = lambda row, col: 0 <= row < n and 0 <= col < n
        queue = [(0, (0,0))] # time to wait, cell
        
        while queue:
            max_so_far, cell = heappop(queue)
            for row_move, col_move in directions:
                new_row = cell[0] + row_move
                new_col = cell[1] + col_move
                if in_range(new_row, new_col):
                    if max(max_so_far, grid[cell[0]][cell[1]], grid[new_row][new_col]) < minimum_time[(new_row, new_col)]:
                        minimum_time[(new_row, new_col)] = max(max_so_far, grid[cell[0]][cell[1]], grid[new_row][new_col])
                        heappush(queue, (minimum_time[(new_row, new_col)], (new_row, new_col)))
                        
        return minimum_time[(n - 1, n - 1)]