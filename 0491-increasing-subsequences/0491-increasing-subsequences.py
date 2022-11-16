class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(path = [], index = 0):
            if len(path) > 1:
                ans.append(path[:])
            
            visited_at_level = set()
            last = path[-1] if path else -101
            for i in range(index, len(nums)):
                if nums[i] in visited_at_level:
                    continue
                
                if nums[i] >= last:
                    path.append(nums[i])
                    backtrack(path, i+1)
                    path.pop()
                
                visited_at_level.add(nums[i])
            
                
        backtrack()
        return ans