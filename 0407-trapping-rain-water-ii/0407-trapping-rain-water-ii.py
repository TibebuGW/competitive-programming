class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        ans = 0
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visited = set()
        queue = []
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    heapq.heappush(queue, (heightMap[i][j], i, j))
                    visited.add((i, j))
        
        while queue:
            cur_height, cur_dx, cur_dy = heapq.heappop(queue)
            
            for dx, dy in directions:
                new_dx, new_dy = cur_dx + dx, cur_dy + dy
                if in_range(new_dx, new_dy) and (new_dx, new_dy) not in visited:
                    if cur_height > heightMap[new_dx][new_dy]:
                        ans += cur_height - heightMap[new_dx][new_dy]
                    visited.add((new_dx, new_dy))
                    heapq.heappush(queue, (max(cur_height, heightMap[new_dx][new_dy]), new_dx, new_dy))
        
        return ans