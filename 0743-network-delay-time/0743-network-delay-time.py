class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = [float('inf')]*n
        ans[k-1] = 0
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        
        queue = [(0, k - 1)]
        
        while queue:
            n = len(queue)
            for i in range(n):
                time, node = heappop(queue)
                for nei, weight in graph[node]:
                    if time + weight < ans[nei]:
                        ans[nei] = time + weight
                        heappush(queue, (ans[nei], nei))
        
        result = max(ans)
        return -1 if result == float('inf') else result