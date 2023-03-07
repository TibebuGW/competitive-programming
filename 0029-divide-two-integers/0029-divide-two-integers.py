class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            sign = -1
        
        quotient = 0
        
        D = abs(dividend)
        d = abs(divisor)
        
        while D >= d:
            multiple = d
            multiplier = 1
            while D >= multiple:
                D -= multiple
                quotient += multiplier
                multiplier += multiplier
                multiple += multiple
        
        if sign == 1:
            return min(2147483647, quotient)
        
        return max(-2147483648, -quotient)
