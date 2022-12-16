class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0]*numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node):
            if color[node] == 2:
                return True
            if color[node] == 1:
                return False
            color[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            color[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True