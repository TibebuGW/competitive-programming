class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move_to_direction_map = {(0, 1): 1, (0, -1): 2, (1, 0): 3, (-1, 0): 4}
        minimum_distance = defaultdict(lambda: float('inf'))
        minimum_distance[(0, 0)] = 0
        queue = [(0, (0, 0))] # minimum cost needed to reach node (x, y)
        
        while queue:
            cost_so_far, cell = heappop(queue)
            
            for row_move, col_move in directions:
                new_row = cell[0] + row_move
                new_col = cell[1] + col_move
                if in_range(new_row, new_col):
                    cur_cost = 0 if grid[cell[0]][cell[1]] == move_to_direction_map[(row_move, col_move)] else 1
                    if cost_so_far + cur_cost < minimum_distance[(new_row, new_col)]:
                        minimum_distance[(new_row, new_col)] = cost_so_far + cur_cost
                        heappush(queue, (minimum_distance[(new_row, new_col)], (new_row, new_col)))
        
        return minimum_distance[(m - 1, n - 1)]