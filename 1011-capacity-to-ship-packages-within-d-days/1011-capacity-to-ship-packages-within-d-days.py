class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        def checkWeight(maxWeight):
            count = 1
            total = 0
            for num in weights:
                total += num
                if total > maxWeight:
                    count += 1
                    total = num
            
            return count <= days
        
        min_ = r
        while l <= r:
            mid = (l + r) // 2
            value = checkWeight(mid)
            if value:
                min_ = min(min_, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_