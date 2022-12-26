class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        prefix = 0
        for num in nums:
            d[prefix] += 1
            prefix += num
            if prefix - k in d:
                count += d[prefix - k]
            
            
        
        return count