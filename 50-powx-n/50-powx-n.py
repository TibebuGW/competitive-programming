class Solution:
    def power(self, num, p):
        if p == 1:
            return num
        if p == 0:
            return 1
        
        value = self.power(num, p//2)
        if p%2 == 0:
            return value*value
        else:
            return value*value*num
    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.power(x, n)
        else:
            return 1/self.power(x, -n)