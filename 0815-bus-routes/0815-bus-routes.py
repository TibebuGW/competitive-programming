class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        node_routes = defaultdict(set)
        
        
        for i, route in enumerate(routes):
            for node in route:
                for c in node_routes[node]:
                    graph[i].add(c)
                    graph[c].add(i)
                node_routes[node].add(i)
        
        steps = 1
        queue = deque([])
        visited = set()
        for num in node_routes[source]:
            queue.append(num)
            visited.add(num)
            
        while queue:
            n = len(queue)
            
            for _ in range(n):
                node = queue.popleft()
                if node in node_routes[target]:
                    return steps
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            steps += 1
        
        
        return -1