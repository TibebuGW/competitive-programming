class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = [float('inf')]*n # cost
        queue = [(-1, 0, src)] # stops, cost, node
        graph = defaultdict(list)
        for start, destination, price in flights:
            graph[start].append((destination, price))
        
        while queue:
            size = len(queue)
            for i in range(size):
                stops, cost, node = heappop(queue)
                for nei, price in graph[node]:
                    if stops + 1 <= k:
                        if ans[nei] > cost + price:
                            ans[nei] = cost + price
                            heappush(queue, (stops + 1, ans[nei], nei))
                        
                    
        return ans[dst] if ans[dst] != float('inf') else -1