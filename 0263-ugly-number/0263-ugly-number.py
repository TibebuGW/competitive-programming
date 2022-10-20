class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1 or n == 2 or n == 3 or n == 5:
            return True
        else:
            for val in [2,3,5]:
                if n%val == 0:
                    if self.isUgly(n//val):
                        return True
            
            return False