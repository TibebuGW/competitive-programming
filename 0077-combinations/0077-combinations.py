class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def backtrack(index = 1):
            if len(path) == k:
                ans.append(path[::])
                return
            
            for i in range(index, n + 1):
                if i not in path:
                    path.append(i)
                    backtrack(i + 1)
                    path.pop()
        
        backtrack()
        return ans