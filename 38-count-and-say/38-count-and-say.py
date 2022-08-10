from collections import Counter
class Solution:
    def say(self, s):
        l = 0
        r = 1
        toReturn = ""
        counter = 1
        while r < len(s):
            if s[r] == s[l]:
                counter += 1
                r += 1
            else:
                toReturn += str(counter) + s[l]
                counter = 1
                l = r
                r += 1
        toReturn += str(counter) + s[l]
        return toReturn
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n-1))