class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src - 1].append((dst - 1, time))
            graph[dst - 1].append((src - 1, time))
        
        minimum_time = [[float('inf'), float('inf')] for _ in range(n)]
        minimum_time[0] = [0, float('inf')]
        queue = [(0, 0)] # time so far, cur_node
        
        
        while queue:
            time_so_far, cur_node = heappop(queue)
            
            for nei, cur_time in graph[cur_node]:
                time_quotient = time_so_far//change
                wait_time = 0
                if time_quotient % 2:
                    limit = (time_quotient + 1) * change
                    wait_time = limit - time_so_far
                
                if time_so_far + wait_time + cur_time < minimum_time[nei][0]:
                    minimum_time[nei][1] = minimum_time[nei][0]
                    minimum_time[nei][0] = time_so_far + wait_time + cur_time
                    heappush(queue, (minimum_time[nei][0], nei))
                else:
                    total_time = time_so_far + wait_time + cur_time 
                    if total_time < minimum_time[nei][1] and total_time > minimum_time[nei][0]:
                        minimum_time[nei][1] = time_so_far + wait_time + cur_time
                        heappush(queue, (minimum_time[nei][1], nei))
        
        return minimum_time[-1][-1]