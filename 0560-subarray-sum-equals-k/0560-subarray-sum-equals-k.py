class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        
        for num in nums:
            prefix += num
            total += d[prefix - k]
            d[prefix] += 1
        
        return total