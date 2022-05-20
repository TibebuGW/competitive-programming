class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0 for _ in range(n+1)]
        
        power_of_2 = 1
        
        for i in range(1, n+1):
            if i == power_of_2<<1:
                bits[i] = 1
                power_of_2 <<= 1
            else:
                base = i - power_of_2
                bits[i] = bits[base] + 1
                
        return bits