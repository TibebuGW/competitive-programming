class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count(num):
            total = 0
            for pile in piles:
                total += math.ceil(pile/num)
            
            return total
        
        left = 1
        right = max(piles)
        best = 0
        while left <= right:
            mid = (left+right)//2
            hour = count(mid)
            if hour <= h:
                best = mid
                right = mid-1
            elif hour > h:
                left = mid+1
        
        return best