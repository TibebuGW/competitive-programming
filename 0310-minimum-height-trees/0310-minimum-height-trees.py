class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        graph = defaultdict(set)
        for fro, to in edges:
            graph[fro].add(to)
            graph[to].add(fro)
        
        queue = deque([i for i in range(n) if len(graph[i]) == 1])
        
        while n > 2:
            
            size = len(queue)
            n -= size
            for _ in range(size):
                node = queue.popleft()
                nei = graph[node].pop()
                graph[nei].remove(node)
                if len(graph[nei]) == 1:
                    queue.append(nei)
        
        return queue