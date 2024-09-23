class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set()
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] += 1
            recipes_set.add(recipes[i])
        
        queue = deque([])
        for supply in supplies:
            queue.append(supply)
            
        ans = []
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0 and nei in recipes_set:
                    ans.append(nei)
                    queue.append(nei)
        
        return ans