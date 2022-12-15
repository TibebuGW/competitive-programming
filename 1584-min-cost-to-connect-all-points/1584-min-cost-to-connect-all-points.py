class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.total_weight = 0
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1, node2, weight):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 != parent2:
            self.parent[parent1] = parent2
            self.total_weight += weight
            
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    edges.append((manhattanDistance(points[i], points[j]), i, j))
        
        edges.sort()
                    
        uf = UnionFind(len(points))
        
        for weight, i, j in edges:
            uf.union(i, j, weight)
        
        
        return uf.total_weight