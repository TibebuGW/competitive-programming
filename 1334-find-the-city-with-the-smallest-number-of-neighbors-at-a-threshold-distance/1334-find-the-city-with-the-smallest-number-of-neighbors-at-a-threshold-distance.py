class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for src, dst, distance in edges:
            graph[src].append((dst, distance))
            graph[dst].append((src, distance))
            
        def Dijkstra(start):
            distances = [float('inf')]*n
            distances[start] = 0
            queue = [(0, start)] # cost, node
            
            while queue:
                size = len(queue)
                for _ in range(size):
                    distance_so_far, node = heappop(queue)
                    for nei, cur_distance in graph[node]:
                        if distance_so_far + cur_distance < distances[nei]:
                            distances[nei] = distance_so_far + cur_distance
                            heappush(queue, ((distances[nei], nei)))
            
            ans = []
            for i in range(len(distances)):
                if 0 < distances[i] <= distanceThreshold:
                    ans.append(i)
            
            return ans
        
        ans = -1
        min_ = float('inf')
        for i in range(n):
            cur_ans = Dijkstra(i)
            if len(cur_ans) <= min_:
                min_ = len(cur_ans)
                ans = i
        
        return ans