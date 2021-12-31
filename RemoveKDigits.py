from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = []
        arr = []
        result = ""
        arr[:0] = num
        # arr = list(num.split(""))
        print(arr)
        
        for n in arr:
            while q and int(n) < int(q[-1]) and k:
                q.pop()
                k -= 1
            q.append(n)
            
        print(q)
        while k:
            q.pop()
            k -= 1
            
        return "0" if q==[] else str(int(result.join(q)))
