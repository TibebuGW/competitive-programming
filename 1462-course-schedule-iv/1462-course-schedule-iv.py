class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prerequisite = [[False for _ in range(numCourses)] for i in range(numCourses)]
        
        for i in range(numCourses):
            is_prerequisite[i][i] = True
            
        for pre, course in prerequisites:
            is_prerequisite[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_prerequisite[i][j] = is_prerequisite[i][j] or (is_prerequisite[i][k] and is_prerequisite[k][j])
        
        return [is_prerequisite[u][v] for u, v in queries]