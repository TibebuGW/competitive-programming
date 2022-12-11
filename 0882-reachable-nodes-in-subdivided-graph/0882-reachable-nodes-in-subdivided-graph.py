class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        ans = 0
        distances = [float('inf')]*n
        distances[0] = 0
        graph = defaultdict(list)
        for src, dst, cnt in edges:
            graph[src].append((dst, cnt + 1))
            graph[dst].append((src, cnt + 1))
        
        queue = [(0, 0)] # distance, node
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cost, node = heappop(queue)
                for nei, weight in graph[node]:
                    if weight + cost < distances[nei]:
                        distances[nei] = weight + cost
                        heappush(queue, (distances[nei], nei))
        
        for distance in distances:
            if distance <= maxMoves:
                ans += 1
        
        for src, dst, cnt in edges:
            moves_from_src = max(0, maxMoves - distances[src])
            moves_from_dst = max(0, maxMoves - distances[dst])
            
            ans += min(moves_from_src + moves_from_dst, cnt)
        
        return ans