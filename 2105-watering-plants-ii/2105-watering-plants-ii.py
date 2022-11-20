class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        half = n//2
        
        originalA = capacityA
        originalB = capacityB
        
        Alice_count = 0
        Bob_count = 0
        
        for i in range(half):
            if plants[i] > capacityA:
                capacityA = originalA
                Alice_count += 1
            capacityA -= plants[i]
            
        for i in range(n-1, n-half-1, -1):
            if plants[i] > capacityB:
                capacityB = originalB
                Bob_count += 1
            capacityB -= plants[i]
        
        
        if n & 1:
            if capacityA >= capacityB:
                if plants[half] > capacityA:
                    Alice_count += 1
            else:
                if plants[half] > capacityB:
                    Bob_count += 1
        
        return Alice_count + Bob_count