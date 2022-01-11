class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def inverter(s) -> str:
            toReturn = ""
            for i in range(len(s)):
                if s[i] == "1":
                    toReturn += "0"
                else:
                    toReturn += "1"
            return toReturn
        
        def outputstr(num) -> str:
            if num == 1:
                return "0"
            x = outputstr(num-1)
            return x + "1" + inverter(x)[::-1]
        
        y = outputstr(n)
        print(y)
        return y[k-1]
