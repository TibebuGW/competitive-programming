class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(i = 0, path = []):
            if i == len(nums):
                ans.append(path[::])
                return
            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            idx = i
            while i < len(nums) and nums[i] == nums[idx]:
                i += 1
            backtrack(i, path)
            
        backtrack()
        return ans