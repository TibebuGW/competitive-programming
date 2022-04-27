class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        rank = [1 for i in range(len(points))]
        result = 0
        paths = []
        def find(a):
            while a != parent[a]:
                a = parent[a]
            return a
        
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a != b:
                if rank[a] > rank[b]:
                    parent[b] = a
                    rank[a] += rank[b]
                else:
                    parent[a] = b
                    rank[b] += rank[a]
                
        def manhattan_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        def connected(p1, p2):
            return find(p1) == find(p2)
        
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                paths.append((manhattan_distance(points[i], points[j]), i, j))
                
        paths.sort(key = lambda x: x[0])
        
        for distance, x, y in paths:
            if not connected(x, y):
                result += distance
                union(x, y)
        
        # print(paths)
        return result
            