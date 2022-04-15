class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = [0]
        n = len(grid)
        m = len(grid[0])
        in_bound = lambda row, col: 0 <= row < n and 0 <= col < m
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        
        def dfs(x,y,count):
            grid[x][y] = 2
            count += 1

            for i in range(len(directions)):
                tempx = x+directions[i][0]
                tempy = y+directions[i][1]
                if in_bound(tempx,tempy) and grid[tempx][tempy] == 1:
                    count += dfs(tempx, tempy, 0)
                    
            return count
                    
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result.append(dfs(i,j,0))
                    # print(isConnected)
                    
        # print(result)
        return max(result)