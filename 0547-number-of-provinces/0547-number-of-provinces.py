class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = [i for i in range(n)]
        
        def find(node):
            if node != parents[node]:
                return find(parents[node])
            return node
        
        def union(node1, node2):
            parent_1 = find(node1)
            parent_2 = find(node2)
            
            parents[parent_2] = parent_1
            
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)
                    
        return len(set([find(num) for num in parents]))