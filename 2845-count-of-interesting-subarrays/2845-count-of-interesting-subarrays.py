class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        total = 0
        d = {0: 1}
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                total += 1
            total %= modulo
            remaining = (total - k) % modulo
            if remaining in d:
                ans += d[remaining]
            
            if total in d:
                d[total] += 1
            else:
                d[total] = 1
        
        return ans