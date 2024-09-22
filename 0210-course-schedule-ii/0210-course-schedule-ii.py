class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0 for _ in range(numCourses)]
        order = []
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[u].append(v)
        
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
            order.append(node)
            return True
        
        for i in range(numCourses):
            if color[i] == 0 and not dfs(i):
                    return []
        
        return order[::-1]