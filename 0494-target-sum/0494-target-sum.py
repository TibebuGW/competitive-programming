class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = [0]
        
        @lru_cache(None)
        def solve(index = 0, score = 0):
            # print(index, score)
            if index == len(nums):
                if score == target:
                    return 1
                else:
                    return 0
            
            return solve(index + 1, score + nums[index]) + solve(index + 1, score - nums[index])
        
        return solve()