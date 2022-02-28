class Solution:
    def days(self, weights, capacity):
        total = count = 0
        
        for i in range(len(weights)):
            if total+weights[i] > capacity:
                count += 1
                total = weights[i]
            else:
                total += weights[i]
                
        return count+1
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right)//2
            temp = self.days(weights, mid)
            print(temp)
            if temp <= days:
                right = mid
            else:
                left = mid+1
            
        return left
