class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_indices = [float('-inf'), float('inf')]
        s_d = {}
        t_d = {}
        
        for char in t:
            if char in t_d:
                t_d[char] += 1
            else:
                t_d[char] = 1
                
        def IsValid():
            for char, quantity in t_d.items():
                if char not in s_d or s_d[char] < quantity:
                    return False
            return True
        
        l = 0
        for r in range(len(s)):
            if s[r] in s_d:
                s_d[s[r]] += 1
            else:
                s_d[s[r]] = 1
            
            while IsValid():
                if ans_indices[1] - ans_indices[0] + 1 > r - l + 1:
                    ans_indices = [l, r]
                
                s_d[s[l]] -= 1
                if s_d[s[l]] == 0:
                    del s_d[s[l]]
                
                l += 1
        
        if ans_indices[0] == float('-inf'):
            return ""
        
        return s[ans_indices[0]:ans_indices[1] + 1]