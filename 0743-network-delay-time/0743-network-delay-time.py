class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = [float('inf')]*n
        ans[k-1] = 0
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        
        queue = [(0, k - 1)]
        visited = set()
        
        while queue:
            time, node = heappop(queue)
            if node in visited:
                continue
            ans[node] = time
            visited.add(node)
            for nei, weight in graph[node]:
                heappush(queue, (time + weight, nei))
        
        result = max(ans)
        return -1 if result == float('inf') else result