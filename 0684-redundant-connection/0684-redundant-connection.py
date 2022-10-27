class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        
        def find(n):
            while n != parent[n]:
                n = parent[n]
                
            return n
        
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a != b:
                parent[a] = b
        
        for start, destination in edges:
            parent_start = find(start-1)
            parent_destination = find(destination-1)
            if parent_start == parent_destination:
                return [start, destination]
            else:
                union(start-1, destination-1)
        
        
        return ans