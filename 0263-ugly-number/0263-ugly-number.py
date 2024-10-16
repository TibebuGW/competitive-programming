class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        
        arr = [2, 3, 5]
        for num in arr:
            if n % num == 0 and self.isUgly(n // num):
                return True
        
        return False
