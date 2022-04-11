from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        color = [0]*numCourses
        orderStack = []
        for course, prerequisite in prerequisites:
            graph[prerequisite].add(course)
        
        cycle = False
        def dfs(node):
            nonlocal cycle
            color[node] = 1
            for child in graph[node]:
                if color[child] == 0:
                    dfs(child)
                if color[child] == 1:
                    cycle = True


            color[node] = 2
            orderStack.append(node)

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)



        return orderStack[::-1] if not cycle else []