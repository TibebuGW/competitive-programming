class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        ans = 0
        for num in nums:
            prefix += num%2
            ans += d[prefix - k]
            d[prefix] += 1
        
        return ans