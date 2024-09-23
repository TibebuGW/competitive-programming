class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        ans = []
        queue = deque([])
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                ans.append(i)
                queue.append(i)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        ans.append(nei)
                        queue.append(nei)
                
        
        return ans if len(ans) == numCourses else []