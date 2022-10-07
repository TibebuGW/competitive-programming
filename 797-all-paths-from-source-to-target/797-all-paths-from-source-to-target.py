class Solution:
    def allPathsSourceTarget(self, dag: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        last = len(dag)-1
        ans = []
        for i, lst in enumerate(dag):
            for val in lst:
                graph[i].append(val)
                
        
        def dfs(node, path):
            nonlocal ans
            path.append(node)
            for destination in graph[node]:
                if destination == last:
                    ans.append(path + [destination])
                else:
                    dfs(destination, path)
            
            path.pop()
        
        dfs(0, [])
        return ans