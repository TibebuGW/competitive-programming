class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)
        
        for i in range(len(s)):
            s_dict[s[i]].append(i)
            t_dict[t[i]].append(i)
            if s_dict[s[i]] != t_dict[t[i]]:
                return False
        
        return True