class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s += "O"
        i = 0
        while i < len(s)-1:
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    total += (d[s[i+1]]-d[s[i]])
                    i += 1
                else:
                    total += d[s[i]]
            elif s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    total += (d[s[i+1]]-d[s[i]])
                    i += 1
                else:
                    total += d[s[i]]
            elif s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    total += (d[s[i+1]]-d[s[i]])
                    i += 1
                else:
                    total += d[s[i]]
            else:
                total += d[s[i]]
            i += 1
            # print(total)
        return total
            