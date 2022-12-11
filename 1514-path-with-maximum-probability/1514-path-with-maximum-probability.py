class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probabilities = [float('inf')]*n
        probabilities[start] = 1
        graph = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            graph[src].append((dst, succProb[i]))
            graph[dst].append((src, succProb[i]))
        
        queue = [(-1, start)] # probability to reach node 
        
        while queue:
            size = len(queue)
            for _ in range(size):
                prob_so_far, node = heappop(queue)
                for nei, cur_prob in graph[node]:
                    if prob_so_far * cur_prob < probabilities[nei]:
                        probabilities[nei] = prob_so_far * cur_prob
                        heappush(queue, (probabilities[nei], nei))
        
        return max(-probabilities[end], 0)