class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return ""
        d = defaultdict(int)
        result = set()
        
        l = 0
        # r = 9
        
        for i in range(len(s)):
            d[s[i:i+10]] += 1
                
        return [key for key, value in d.items() if value > 1]