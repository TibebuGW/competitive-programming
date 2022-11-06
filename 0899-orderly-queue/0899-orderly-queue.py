class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = list(s)
        if k >= 2:
            s.sort()
            return "".join(s)
        else:
            min_ = ["z"]*1000
            for i in range(len(s)):
                min_ = min(min_, s[i:]+s[:i])
            
            return "".join(min_)