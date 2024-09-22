class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        colors = [0 for _ in range(numCourses)]
        
        def dfs(node):
            if colors[node] == 2:
                return True
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            colors[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True