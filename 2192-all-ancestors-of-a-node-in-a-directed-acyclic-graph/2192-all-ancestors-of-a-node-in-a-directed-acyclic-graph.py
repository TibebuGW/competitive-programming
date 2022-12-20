class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        
        graph = defaultdict(list)
        incoming = [0 for _ in range(n)]
        
        for fro, to in edges:
            graph[fro].append(to)
            incoming[to] += 1
        queue = deque()
        
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            level = len(queue)
            
            for _ in range(level):
                curr = queue.popleft()
                
                for nei in graph[curr]:
                    ancestors[nei].update(ancestors[curr])
                    ancestors[nei].add(curr)
                    incoming[nei] -= 1
                    
                    if incoming[nei] == 0:
                        queue.append(nei)
                        
        for i in range(n):
            ancestors[i] = sorted(list(ancestors[i]))
        
        return ancestors