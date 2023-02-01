class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        total = 0
        for i in range(k):
            if blocks[i] == "W":
                total += 1
        
        min_ = total
        l = 0
        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                total += 1
            
            if blocks[l] == "W":
                total -= 1
            
            l += 1
            
            min_ = min(min_, total)
        
        return min_