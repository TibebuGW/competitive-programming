class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def backtrack(i = 1, total = 0):
            if total == n and len(path) == k:
                ans.append(path[::])
                return
            
            if i > 9:
                return
            
            if len(path) + 1 <= k and total + i <= n:
                path.append(i)
                total += i
                backtrack(i + 1, total)
                total -= i
                path.pop()
            
            backtrack(i + 1, total)
            
        backtrack()
        
        return ans