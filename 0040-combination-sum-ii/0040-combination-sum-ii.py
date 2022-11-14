class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(path, total_so_far, index):
            if total_so_far == target:
                ans.append(path[::])
                return
            
            if index == len(candidates):
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if total_so_far + num <= target:
                    path.append(num)
                    total_so_far += num
                    backtrack(path, total_so_far, i+1)
                    path.pop()
                    total_so_far -= num
                else:
                    break
            
            return
        
        backtrack([], 0, 0)
        
        return ans