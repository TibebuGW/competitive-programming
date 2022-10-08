class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for_0 = 0
        for_1 = float("-inf")
        
        for num in prices:
            for_0 = max(for_0, for_1+num)
            for_1 = max(for_1, -num)
        
        # print(for_0, for_1)
        return for_0