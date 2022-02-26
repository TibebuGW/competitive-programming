"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def middleware(self, customFunction, x, z):
        left = 1
        right = 1000
        while left <= right:
            mid = (left+right)//2
            if customFunction.f(x,mid) < z:
                left = mid+1
            elif customFunction.f(x,mid) > z:
                right = mid-1
            else:
                return mid
        
        return -1
                
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        
        for i in range(1, 1001):
            x = i
            y = self.middleware(customfunction, x, z)
            if y != -1:
                result.append([x,y])
                
        return result
