from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = -1
        m = len(grid)
        n = len(grid[0])
        in_bound = lambda row, col: 0 <= row < m and 0 <= col < n
        count1 = 0
        queue = deque()
        d = [[0,1], [0,-1], [1,0], [-1,0]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count1 += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                    
        if count1 == 0:
            return 0
        
        while queue:
            result += 1
            # print(queue)
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                for i in range(len(d)):
                    if in_bound(temp[0]+d[i][0], temp[1]+d[i][1]) and grid[temp[0]+d[i][0]][temp[1]+d[i][1]] == 1:
                        grid[temp[0]+d[i][0]][temp[1]+d[i][1]]=2 
                        count1 -= 1
                        queue.append((temp[0]+d[i][0],temp[1]+d[i][1]))
                    
        if count1 == 0:
            return result
        else:
            return -1
            