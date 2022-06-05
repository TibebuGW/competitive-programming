class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    
        def floydWarshall(reachable):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
            
            return reachable
            
        
        adjMatrix =  [[ 0 for i in range(n)] for j in range(n)]
        for i in prerequisites:
            adjMatrix[i[0]][i[1]] = 1
        
        #print(adjMatrix)
        ans = []
        floydWarshall(adjMatrix)
        #print(adjMatrix)
        for i in queries:
            ans.append(bool(adjMatrix[i[0]][i[1]]))
        
        return ans