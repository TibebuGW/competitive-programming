class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for pre, curr in prerequisites:
            graph[curr].add(pre)
            graph[curr].update(graph[pre])
        
        for pre, curr in prerequisites[::-1]:
            graph[curr].add(pre)
            graph[curr].update(graph[pre])
        ans = []
        for u, v in queries:
            ans.append(u in graph[v])
        
        return ans