class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        for_0 = 0
        for_1 = float('-inf')
        
        for num in prices:
            for_0 = max(for_0, for_1+num-fee)
            for_1 = max(for_1, for_0-num)
        
        return for_0