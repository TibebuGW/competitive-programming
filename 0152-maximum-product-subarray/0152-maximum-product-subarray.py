class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        max_ = 1
        min_ = 1
        
        for num in nums:
            new_max_ = max(max_ * num, min_ * num, num)
            new_min_ = min(max_ * num, min_ * num, num)
            max_ = new_max_
            min_ = new_min_
            ans = max(ans, max_)
            
        return ans