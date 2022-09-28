class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_d = defaultdict(int)
        t_d = defaultdict(int)
        
        for char in t:
            t_d[char] += 1
            
        def is_valid():
            for key, val in t_d.items():
                if s_d[key] < t_d[key]:
                    return False
            return True
                    
        
        l = 0
        bl, br = 0, len(s)
        for r in range(len(s)):
            s_d[s[r]] += 1
            while is_valid():
                if (br-bl+1) > (r-l+1):
                    br, bl = r, l
                s_d[s[l]] -= 1
                l += 1
        
        if (br-bl+1 == len(s)+1): return ""
        return s[bl:br+1]
                        