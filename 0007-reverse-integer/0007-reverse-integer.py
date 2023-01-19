class Solution:
    def reverse(self, x: int) -> int:
        in_bound = lambda num: -(2**31) <= num <= 2**31
        
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            reverse = (reverse*10) + x%10
            x //= 10
        
        if not in_bound(sign*reverse):
            return 0
        return sign*reverse