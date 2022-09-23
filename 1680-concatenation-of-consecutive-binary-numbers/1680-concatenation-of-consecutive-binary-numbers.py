class Solution:
    def concatenatedBinary(self, n: int) -> int:
        arr = []
        
        for i in range(1, n+1):
            b = bin(i)[2:]
            arr.append(b)
        
        return (int("".join(arr), 2))%(1000000007)
        