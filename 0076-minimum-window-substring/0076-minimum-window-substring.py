class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ascii_limit = 65 if 65<=ord(s[0])<=90 else 97
        ans = [float('-inf'), float('inf')]
        s_d = defaultdict(int)
        t_d = defaultdict(int)
        for char in t:
            t_d[char] += 1
        
        l = 0
        for r in range(len(s)):
            s_d[s[r]] += 1
            flag = True
            for key, val in t_d.items():
                if s_d[key] < val:
                    flag = False
            
            if flag:
                while l <= r:
                    if s_d[s[l]]-1 >= t_d[s[l]]:
                        s_d[s[l]] -= 1
                        l += 1
                    else:
                        break
                
                if r-l < ans[1]-ans[0]:
                    # print(l,r)
                    ans = [l, r]
                    
        # print(ans)
        return s[ans[0]:ans[1]+1] if ans[0] != float('-inf') else ""