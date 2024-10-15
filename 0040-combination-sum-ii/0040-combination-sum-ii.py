class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        
        def backtrack(i = 0, total = 0):
            if total == target:
                ans.append(path[::])
                return
            if i == len(candidates):
                return
            
            if total + candidates[i] <= target:
                path.append(candidates[i])
                total += candidates[i]
                backtrack(i + 1, total)
                total -= candidates[i]
                path.pop()
            
            idx = i
            while i < len(candidates) and candidates[i] == candidates[idx]:
                i += 1
            backtrack(i, total)
        
        backtrack()
        return ans