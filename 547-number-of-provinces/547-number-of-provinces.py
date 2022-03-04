class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        result = 0
        n = len(isConnected)
        in_bound = lambda row, col: 0 <= row < n and 0 <= col < n
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        
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
            