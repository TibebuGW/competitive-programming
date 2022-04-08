from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        outDegree = defaultdict(set)
        
        for course, pre in prerequisites:
            inDegree[course] += 1
            outDegree[pre].add(course)
            
        # print(inDegree)
        # print(outDegree)
        result = []
        queue = deque([])
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                result.append(i)
                
        count = 0
        # print("abc")
        
        while queue:
            node = queue.popleft()
            if node not in result: result.append(node)
            count += 1
            for j in outDegree[node]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    queue.append(j)
                    
        return result if count == numCourses else []