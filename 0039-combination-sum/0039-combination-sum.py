class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(path, total_so_far, index):
            if total_so_far == target:
                ans.append(path[::])
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num + total_so_far <= target:
                    path.append(num)
                    backtrack(path, total_so_far + num, i)
                    path.pop()
            
            return
        
        backtrack([], 0, 0)
        return ans