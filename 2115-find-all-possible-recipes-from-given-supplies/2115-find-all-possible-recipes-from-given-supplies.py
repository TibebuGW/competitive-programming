from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:                
        # print(graph)
        inDegree = defaultdict(int)
        graph = defaultdict(set)
        for i in range(len(ingredients)):
            for supply in ingredients[i]:
                graph[supply].add(recipes[i])
                inDegree[recipes[i]] += 1
                
        queue = deque([])
        for supply in supplies:
            queue.append(supply)
            
        ans = []
        while queue:
            node = queue.popleft()
            for recipe in graph[node]:
                inDegree[recipe] -= 1
                if inDegree[recipe] == 0:
                    ans.append(recipe)
                    queue.append(recipe)
                    
        return ans
        
        