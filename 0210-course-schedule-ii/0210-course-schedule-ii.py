class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0]*numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        ordering = []
        def dfs(node):
            if color[node] == 2:
                return True
            if color[node] == 1:
                return False
            
            color[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
                
            ordering.append(node)
            color[node] = 2
            return True
        
        for i in range(numCourses):
            if color[i] == 0 and not dfs(i):
                return []
        
        return ordering[::-1]