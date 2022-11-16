class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def backtrack(path, index):
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                ans.append(path[:])
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)
        return ans