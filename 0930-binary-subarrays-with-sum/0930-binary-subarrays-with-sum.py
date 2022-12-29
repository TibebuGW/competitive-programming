class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        prefix = 0
        d = defaultdict(int)
        
        for num in nums:
            d[prefix] += 1
            prefix += num
            ans += d[prefix - goal]
        
        return ans