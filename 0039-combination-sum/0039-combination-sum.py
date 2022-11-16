class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(path = [], total_sum = 0, index = 0):
            if total_sum == target:
                ans.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num + total_sum <= target:
                    path.append(num)
                    total_sum += num
                    backtrack(path, total_sum, i)
                    total_sum -= num
                    path.pop()
        
        backtrack()
        return ans