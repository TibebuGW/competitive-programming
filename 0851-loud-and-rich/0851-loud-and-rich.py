class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for fro, to in richer:
            graph[fro].append(to)
            
        ans = [[float('inf'), n] for i in range(n)]
        
        @lru_cache(None)
        def dfs(cur_node, min_quiet_node, min_quiet):
            if ans[cur_node][0] > min_quiet:
                ans[cur_node][0] = min_quiet
                ans[cur_node][1] = min_quiet_node
                
            for nei in graph[cur_node]:
                dfs(nei, ans[cur_node][1], ans[cur_node][0])
            
                    
        for i in range(n):
            dfs(i, i, quiet[i])
        
        return [node for val, node in ans]