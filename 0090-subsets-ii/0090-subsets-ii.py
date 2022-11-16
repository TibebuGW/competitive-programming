class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def backtrack(path = [], index = 0):
            if path:
                ans.append(path[:])
            
            visited_at_level = set()
            for i in range(index, len(nums)):
                if nums[i] not in visited_at_level:
                    path.append(nums[i])
                    backtrack(path, i+1)
                    path.pop()

                    visited_at_level.add(nums[i])
                
        
        backtrack()
        return ans