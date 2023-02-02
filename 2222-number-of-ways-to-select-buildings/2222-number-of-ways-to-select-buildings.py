class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        dp_01 = int(s[-2:] == "01")
        dp_10 = int(s[-2:] == "10")
        dp_1 = 0
        dp_0 = 0
        for i in range(n - 2, n):
            if s[i] == "0":
                dp_0 += 1
            else:
                dp_1 += 1
        total = 0
        
        for i in range(n - 3, -1, -1):
            if s[i] == "1":
                total += dp_01
                dp_10 += dp_0
                dp_1 += 1
            else:
                total += dp_10
                dp_01 += dp_1
                dp_0 += 1
        
        return total