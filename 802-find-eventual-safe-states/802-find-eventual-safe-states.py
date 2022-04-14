class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 1-white, 2-grey, 3-black
        result = []
        n = len(graph)
        color = [0]*n
        
        def dfs(node):
            if color[node] == 2:
                return True
            if color[node] == 1:
                return False
            
            color[node] = 1
            for child in graph[node]:
                if color[child] == 1:
                    return False
                elif color[child] == 0:
                    if dfs(child):
                        continue
                    else:
                        return False
            
            color[node] = 2
            return True
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        
        # print(color)
        return result