class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        node_info = [[0, 0] for _ in range(n)] # [in_degree, max_time_spent_before_this_course]
        ans = 0
        graph = defaultdict(list)
        for u, v in relations:
            graph[u - 1].append(v - 1)
            node_info[v - 1][0] += 1
        
        queue = deque([])
        
        for i in range(n):
            if node_info[i][0] == 0:
                queue.append((i, time[i])) # it takes time[i] months to finish course i and all it's prerequisites
        
        while queue:
            node, max_time_spent_before_this_course = queue.popleft()
            ans = max(ans, max_time_spent_before_this_course)
            for nei in graph[node]:
                node_info[nei][0] -= 1
                node_info[nei][1] = max(node_info[nei][1], max_time_spent_before_this_course)
                if node_info[nei][0] == 0: # all prerequisites are finished
                    queue.append((nei, node_info[nei][1] + time[nei]))
        
        return ans