class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(path, visited):
            if len(path) == len(nums):
                ans.append(path[::])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(path, visited)
                    path.pop()
                    visited.remove(nums[i])
            
        backtrack([], set())
        return ans