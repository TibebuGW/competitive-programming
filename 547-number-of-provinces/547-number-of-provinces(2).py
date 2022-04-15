class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        
        def find(n):
            while n != parent[n]:
                n = parent[n]
                
            return n
        
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a != b:
                parent[a] = b
                
        
        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i,j)
        
        print(parent)
        return len(set([find(i) for i in range(len(isConnected))]))           
