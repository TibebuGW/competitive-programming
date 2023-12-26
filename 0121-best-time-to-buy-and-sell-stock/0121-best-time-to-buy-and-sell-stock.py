class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = float('-inf')
        
        min_ = float('inf')
        
        for num in prices:
            min_ = min(min_, num)
            max_ = max(max_, num - min_)
        
        return max_