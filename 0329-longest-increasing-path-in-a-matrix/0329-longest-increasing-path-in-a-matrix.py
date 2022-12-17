from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        in_degree = {(i, j): 0 for i in range(m) for j in range(n)}
        graph = defaultdict(list)
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        
        for i in range(m):
            for j in range(n):
                for row_move, col_move in directions:
                    row = i + row_move
                    col = j + col_move
                    if in_range(row, col) and matrix[i][j] < matrix[row][col]:
                        in_degree[(row, col)] += 1
                        graph[(i,j)].append((row, col))
        
        @lru_cache(None)
        def dfs(i, j):
            max_ = 1
            for nei in graph[(i, j)]:
                max_ = max(max_, dfs(nei[0], nei[1]) + 1)
            return max_
        
        ans = 0
        for node, in_degree_value in in_degree.items():
            if in_degree_value == 0:
                # print(bfs(node[0], node[1]), node)
                ans = max(ans, dfs(node[0], node[1]))
        
        return ans