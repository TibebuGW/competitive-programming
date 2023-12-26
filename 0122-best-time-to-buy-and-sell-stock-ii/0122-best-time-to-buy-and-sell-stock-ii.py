class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        total = 0
        
        for num in prices:
            if num > min_so_far:
                total += (num - min_so_far)
            min_so_far = num
        
        return total