class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        n = len(plants)
        original = capacity
        
        for i in range(n):
            if capacity < plants[i]:
                capacity = original
                count += 2*i
            capacity -= plants[i]
            
            count += 1
        
        return count