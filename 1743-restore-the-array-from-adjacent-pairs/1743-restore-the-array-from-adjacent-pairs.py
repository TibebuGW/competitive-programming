class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, destination in adjacentPairs:
            graph[start].append(destination)
            graph[destination].append(start)
        
        ans = []
        def dfs(node, parent):
            ans.append(node)
            
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
            
            return
    
        for key, val in graph.items():
            if len(val) == 1:
                dfs(key, float('-inf'))
                break
        return ans