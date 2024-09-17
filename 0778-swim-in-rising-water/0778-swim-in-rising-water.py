class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_range = lambda x, y: 0 <= x < n and 0 <= y < n
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = set()
        min_time = defaultdict(lambda x: float('inf'))
        queue = []
        
        heapq.heappush(queue, (grid[0][0], 0, 0))
        
        while queue:
            cost, cur_dx, cur_dy = heapq.heappop(queue)
            if (cur_dx, cur_dy) in visited:
                continue
            min_time[(cur_dx, cur_dy)] = cost
            visited.add((cur_dx, cur_dy))
            for dx, dy in directions:
                new_dx, new_dy = cur_dx + dx, cur_dy + dy
                if in_range(new_dx, new_dy):
                    heappush(queue, (max(cost, grid[new_dx][new_dy]), new_dx, new_dy))
        
        return min_time[(n - 1, m - 1)]