class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        nodes = set()
        for i, equation in enumerate(equations):
            graph[equation[0]].append((equation[1], values[i]))
            graph[equation[1]].append((equation[0], 1/values[i]))
            nodes.add(equation[0])
            nodes.add(equation[1])
        
        
        def dfs(node, visited, target, total):
            
            if node == target:
                return total
            
            max_ = -1.0
            for nei, cost in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    max_ = max(max_, dfs(nei, visited, target, total * cost))
                    visited.remove(nei)
            
            return max_
        
        ans = []
        for start, destination in queries:
            if start not in nodes or destination not in nodes:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, set(), destination, 1))
        
        return ans