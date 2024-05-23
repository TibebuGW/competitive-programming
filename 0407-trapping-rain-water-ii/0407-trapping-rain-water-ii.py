class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        ans = 0
        visited = set()
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        in_range = lambda x, y: 0 <= x < n and 0 <= y < m
        heap = []
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
                    
        while heap:
            cur_height, cur_x, cur_y = heapq.heappop(heap)
            for dx, dy in directions:
                nei_dx, nei_dy = cur_x + dx, cur_y + dy
                if in_range(nei_dx, nei_dy) and (nei_dx, nei_dy) not in visited:
                    visited.add((nei_dx, nei_dy))
                    if heightMap[nei_dx][nei_dy] < cur_height:
                        ans += cur_height - heightMap[nei_dx][nei_dy]
                    heapq.heappush(heap, (max(cur_height, heightMap[nei_dx][nei_dy]), nei_dx, nei_dy))
        
        return ans