class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        edge_count = [0 for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            edge_count[u] += 1
            edge_count[v] += 1
        
        queue = deque([])
        for i in range(n):
            if edge_count[i] == 1 or edge_count[i] == 0:
                queue.append(i)
                
        while n > 2:
             
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        queue.append(nei)
        
            n -= size
        
        return queue