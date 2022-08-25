class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def recursion(n):
            print(n)
            if n == 1:
                return True
            if n%3 != 0 or n < 1:
                return False
            
            return recursion(n//3)
        
        return recursion(n)