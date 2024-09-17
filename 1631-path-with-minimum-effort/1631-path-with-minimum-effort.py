class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        distances = {}
        
        queue = [(0, 0, 0)]
        visited = set()
        
        while queue:
            cost, x, y = heapq.heappop(queue)
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            distances[(x, y)] = cost
            
            for row_move, col_move in directions:
                new_row = row_move + x
                new_col = col_move + y
                if in_range(new_row, new_col):
                    heapq.heappush(queue, (max(cost, abs(heights[x][y] - heights[new_row][new_col])), new_row, new_col))
        
        return distances[(n - 1, m - 1)]