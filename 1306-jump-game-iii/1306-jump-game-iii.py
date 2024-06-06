class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        in_range = lambda x: 0 <= x < len(arr)
        visited = set()
        
        @lru_cache(None)
        def dfs(index = start):
            nonlocal visited
            if not in_range(index) or index in visited:
                return False
            
            if arr[index] == 0:
                return True
            
            visited.add(index)
            left = dfs(index - arr[index])
            right = dfs(index + arr[index])
            visited.remove(index)
            return left or right
        
        return dfs()