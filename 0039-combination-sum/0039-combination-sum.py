class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def backtrack(i = 0, total = 0):
            if i == len(candidates):
                return
            if total == target:
                ans.append(path[:])
                return
            
            if total + candidates[i] <= target:
                path.append(candidates[i])
                total += candidates[i]
                backtrack(i, total)
                total -= candidates[i]
                path.pop()
            
            backtrack(i + 1, total)
        
        backtrack()
        
        return ans