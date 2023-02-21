class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(n)]
        for start, end in edges:
            indegree[end] += 1
        
        ans = []

        for i, num in enumerate(indegree):
            if num==0:
                ans.append(i)
                
        return ans