class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        result = 0
        n = len(isConnected)
        
        def dfs(row):

            for i in range(n):
                if row == i:
                    isConnected[row][i] = 2
                    continue
                if isConnected[row][i] == 1:
                    isConnected[row][i] = 2
                    visited.add(i)
                    dfs(i)
            
        for i in range(n):
            if i not in visited:
                visited.add(i)
                result += 1
                dfs(i)
                    
        return result
            
