class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        mask = (1 << n) - 1
        path = []
        
        def backtrack(i = 0):
            nonlocal mask
            
            if not mask:
                ans.append(path[::])
                return
            
            for j in range(n):
                if mask & (1 << j):
                    mask ^= (1 << j)
                    path.append(nums[j])
                    backtrack(j + 1)
                    path.pop()
                    mask ^= (1 << j)
            
        backtrack()
        return ans