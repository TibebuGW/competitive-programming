class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(n*m)]
        # print(parent)
        directions = [[0,-1],[-1,0]]
        in_range = lambda row, col: 0 <= row < m and 0 <= col < n
        # graph = defaultdict(list)
        
        # for i in range(n):
        #     for j in range(m):
                        
                
        rank = [grid[i][j] for i in range(m) for j in range(n)]
        # print(rank)
        
        def find(a):
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a, b):
            # print("num1:", a)
            # print("num2:", b)
            a = find(a)
            b = find(b)
            
            if a != b:
                if rank[a] > rank[b]:
                    parent[b] = a
                    rank[a] += rank[b]
                else:
                    parent[a] = b
                    rank[b] += rank[a]
            
            # print(rank)
                    
        for i in range(m):
            for j in range(n):
                # print("subject:", (i*m)+j)
                if grid[i][j] == 1:
                    # print("i:", i, "j:", j, "grid value:", grid[i][j])
                    for k in range(2):
                        nei_i = i+directions[k][0]
                        nei_j = j+directions[k][1]
                        if in_range(nei_i,nei_j) and grid[nei_i][nei_j] == 1:
                            union((i*n)+j, (nei_i*n)+nei_j)
                    
        # print(parent)
        # print(rank)
        # mmax = 0
        # print(grid)
        return max([rank[find(i)] for i in parent])
        # d = collections.Counter(parent)
        # print(d)