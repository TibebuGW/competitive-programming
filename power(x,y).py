class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solver(base, power) -> float:
            if power == 2:
                return base*base
            if power == 1:
                return base
            
            y = base if power%2 == 1 else 1
            return solver(base*base, power//2)*y
        
        
        
        if n == 0:
            return 1
        elif n > 0:
            return solver(x, n)
        else: 
            return 1/solver(x, abs(n))
