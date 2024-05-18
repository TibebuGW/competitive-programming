class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int) # d[x] = 0
        total = 0
        ans = 0
        
        for num in nums:
            d[total] += 1
            total += num
            ans += d[total - goal]
        
        return ans