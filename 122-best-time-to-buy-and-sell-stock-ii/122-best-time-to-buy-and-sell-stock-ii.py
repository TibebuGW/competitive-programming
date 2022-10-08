class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for_0 = 0
        for_1 = float('-inf')
        
        for num in prices:
            # print(for_1)
            prev = for_0
            for_0 = max(for_0, for_1+num)
            for_1 = max(for_1, prev-num)
        
        # print(for_1, for_0)
        return for_0