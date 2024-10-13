class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst, weight in edges:
            graph[src - 1].append((dst - 1, weight))
            graph[dst - 1].append((src - 1, weight))
        
        distances = [float('inf')]*n
        distances[-1] = 0
        
        queue = [(0, n - 1)] # shortest path to node n
        
        while queue:
            distance_so_far, node = heappop(queue)
            
            for nei, weight in graph[node]:
                if distance_so_far + weight < distances[nei]:
                    distances[nei] = distance_so_far + weight
                    heappush(queue, (distances[nei], nei))
        
        
        @lru_cache(None)
        def dp(node = 0):
            if node == n - 1:
                return 1
            
            ans = 0
            for nei, weight in graph[node]:
                if distances[node] > distances[nei]:
                    ans += dp(nei)
            
            return ans
        
        return dp() % 1_000_000_007