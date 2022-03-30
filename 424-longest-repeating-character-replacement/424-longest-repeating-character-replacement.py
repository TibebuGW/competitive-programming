class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 1
        d = defaultdict(int)
        
        l = 0
        biggest = 0
        
        for r in range(len(s)):
            d[s[r]] += 1
            biggest = max(biggest, d[s[r]])
            
            if (r-l+1)-biggest > k:
                d[s[l]] -= 1
                l += 1
                
            result = max(result, r-l+1)
            
            r += 1
    
        return result