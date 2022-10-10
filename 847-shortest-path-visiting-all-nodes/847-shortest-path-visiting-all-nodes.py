class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        min_ = float('inf')
        for i in range(len(graph)):
            min_ = min(min_, len(graph[i])) 
        level = 0
        visited = set()
        queue = deque([(i, 1<<i) for i in range(len(graph)) if len(graph[i]) == min_])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node[1].bit_count() == len(graph):
                    return level
                for nei in graph[node[0]]:
                    if (nei, node[1] | (1<<nei)) not in visited:
                        queue.append((nei, node[1] | (1<<nei)))
                        visited.add((nei, node[1] | (1<<nei)))
            level += 1
                    