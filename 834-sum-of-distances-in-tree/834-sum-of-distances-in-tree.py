class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        
        result = [0]*n
        count = [1]*n
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    result[node] += result[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    result[child] = result[node] - count[child] + (n-count[child])
                    
                    dfs2(child, node)
                    
        dfs(0,None)
        dfs2(0, None)
        return result
        