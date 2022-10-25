class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        d = defaultdict(list)
        hash_value = 0
        hash_prime = 7
        power = 0
        for i in range(10):
            hash_value += ((ord(s[i])-64)*(hash_prime**power))
            power += 1
        power -= 1
        l = 0
        d[hash_value].append((s[:10], l, 9))
        for r in range(10, len(s)):
            hash_value -= ord(s[l])-64
            l += 1
            hash_value //= hash_prime
            hash_value += ((ord(s[r])-64)*(hash_prime**power))
            d[hash_value].append((s[l:r+1], l, r))
        
        # print(d)
        result = []
        for key, val in d.items():
            if len(val) > 1:
                # print([key, val])
                result.append(val[0][0])
        
        
        return result