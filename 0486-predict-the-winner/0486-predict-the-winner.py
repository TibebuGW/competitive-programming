class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        # figure out the maximum possible score player 1 can get.
        @lru_cache(None)
        def recursion(left, right):
            
            # base case
            if left == right:
                return nums[right]
            
            if left > right:
                return 0
            
            option1 = nums[left] + min(recursion(left + 1, right - 1), recursion(left + 2, right))
            option2 = nums[right] + min(recursion(left, right - 2), recursion(left + 1, right - 1))
            
            return max(option1, option2)
        
        # check if his score is greater than the max of the total sum.
        player_one_score = recursion(0, len(nums) - 1)
        total = sum(nums)
        player_two_score = total - player_one_score
        return player_one_score >= player_two_score