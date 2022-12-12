class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        efforts = defaultdict(lambda: float('inf'))
        efforts[(0,0)] = 0
        queue = [(0,(0,0))] # effort_so_far, cell
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        in_range = lambda row, col: 0 <= row < n and 0 <= col < m
        
        
        while queue:
            effort_so_far, cell = heappop(queue)
            
            for row_move, col_move in directions:
                new_row = cell[0] + row_move
                new_col = cell[1] + col_move
                if in_range(new_row, new_col):
                    if max(effort_so_far, abs(heights[new_row][new_col] - heights[cell[0]][cell[1]])) < efforts[(new_row, new_col)]:
                        efforts[(new_row, new_col)] = max(effort_so_far, abs(heights[new_row][new_col] - heights[cell[0]][cell[1]]))
                        heappush(queue, (efforts[(new_row, new_col)], (new_row, new_col)))
        
        return efforts[(n - 1, m - 1)]