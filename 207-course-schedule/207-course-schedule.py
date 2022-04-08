from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        outDegree = defaultdict(set)
        
        for course, pre in prerequisites:
            inDegree[course] += 1
            outDegree[pre].add(course)
            
        # print(inDegree)
        # print(outDegree)
        
        queue = deque([])
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            for j in outDegree[node]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    queue.append(j)
                    
        return count == numCourses