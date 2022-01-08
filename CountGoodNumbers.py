class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 1000000007
        if n == 2:
            return 20
        if n == 1:
            return 5
        
        d = 5 if n%2 == 1 else 1
        
        return (20**(n//2)*d)%m
