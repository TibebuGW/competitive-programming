from itertools import permutations
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n&n-1
    
    def reorderedPowerOf2(self, n: int) -> bool:
        p = set(permutations(str(n)))
        arr = []
        # print(p)
        for num in p:
            if num[0] != "0":
                s = "".join(num)
                arr.append(int(s))
        
        # print(arr)
        for num in arr:
            if self.isPowerOfTwo(num):
                return True
        
        return False