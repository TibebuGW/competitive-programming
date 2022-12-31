class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(path = [], total_sum = 0, index = 0):
            if total_sum == target:
                ans.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if num + total_sum <= target:
                    path.append(num)
                    total_sum += num
                    backtrack(path, total_sum, i+1)
                    total_sum -= num
                    path.pop()
        
        backtrack()
        return ans