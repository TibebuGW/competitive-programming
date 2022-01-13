class Solution:
    
    def middleware(self, c, d):
        if c == 0:
            if d%2 == 0:
                return 1
            else:
                return 0
        else:
            if d%2 == 0:
                return 0
            else:
                return 1
            
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if n == 2 and k == 1:
            return 0
        if n == 2 and k == 2:
            return 1
        # print(n, k)
        return self.middleware(self.kthGrammar(n-1, ceil(k/2)), k)
            
        
