class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            
            smallest_1 = float('inf')
            index_1 = -1
            for index, num in enumerate(grid[i-1]):
                if num < smallest_1:
                    smallest_1 = num
                    index_1 = index
            
            smallest_2 = float('inf')
            index_2 = -1
            for index, num in enumerate(grid[i-1]):
                if num < smallest_2 and index != index_1:
                    smallest_2 = num
                    index_2 = index
            
            for j in range(len(grid[i])):
                if j != index_1:
                    grid[i][j] += smallest_1
                else:
                    grid[i][j] += smallest_2
        
        return min(grid[-1])