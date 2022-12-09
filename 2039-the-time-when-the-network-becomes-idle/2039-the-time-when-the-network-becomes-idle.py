class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        distances = [float('inf')]*n
        distances[0] = 0
        graph = defaultdict(list)
        for source, destination in edges:
            graph[source].append((destination, 1))
            graph[destination].append((source, 1))
        
        queue = [(0, 0)]
        
        while queue:
            size = len(queue)
            for i in range(size):
                distance, node = heappop(queue)
                for nei, weight in graph[node]:
                    if distance + weight < distances[nei]:
                        distances[nei] = distance + weight
                        heappush(queue, (distances[nei], nei))
        
        max_ = -1
        for i in range(1, n):
            cur_limit = 2*distances[i]
            last_signal_sent = ((cur_limit-1)//patience[i]) * patience[i]
            max_ = max(max_, cur_limit + last_signal_sent)
        return max_ + 1