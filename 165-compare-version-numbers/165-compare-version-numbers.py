class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")
        
        r = max(len(a), len(b))
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b.append("0")
        elif len(a) < len(b):
            for i in range(len(b)-len(a)):
                a.append("0")
                
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) < int(b[i]):
                return -1
                
        return 0
        
        