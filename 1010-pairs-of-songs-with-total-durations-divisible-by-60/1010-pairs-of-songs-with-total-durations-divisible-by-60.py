class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for num in time:
            if num % 60 == 0:
                d[60] += 1
                continue
            ans += d[60 - (num % 60)]
            d[num % 60] += 1
        
        
        return int(ans + ((factorial(d[60])/(factorial(max(d[60] - 2, 0)) * 2))))