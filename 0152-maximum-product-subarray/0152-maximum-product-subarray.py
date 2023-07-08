class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = 1
        max_ = 1
        ans = float('-inf')
        
        for num in nums:
            temp = min_
            min_ = min(num, min_*num, max_*num)
            max_ = max(num, max_*num, temp*num)
        
            ans = max(ans, max_)
        
        return ans