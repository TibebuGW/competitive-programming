class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf') for _ in range(n)]
        distances[k - 1] = 0
        queue = []
        graph = defaultdict(list)
        visited = set()
        
        for u, v, w in times:
            graph[u - 1].append((w, v - 1))
        queue.append((0, k - 1))
        
        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            distances[node] = cost
            visited.add(node)
            for cost_from, nei in graph[node]:
                heapq.heappush(queue, (cost + cost_from, nei))
        
        if float('inf') in distances:
            return -1
        
        return max(distances)