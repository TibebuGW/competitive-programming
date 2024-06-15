class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # The goal of this question is remove the smallest subarray such that
        # the sum of the remaining elements is divisible by p. To keep the
        # rest of the elements sum up to be divisible by p, the remainder should
        # be removed. This is target = sum(nums) % p. That means the subarray's 
        # sum when modulo-ed by p should be target. The trick comes when using
        # prefix sum. The sum we're looking for is prefix[j] - prefix[i]. We're 
        # at j but we don't know i. The remainder of prefix[j] is cur = prefix[j] % p
        # If we're looking for a remainder target and we have cur, the difference of
        # the two is what we should look for i. That means cur - target. But this 
        # value can be negative. To counter that we need to mod it again with p.
        
        
        prefix = 0
        d = {0: -1}
        ans = float('inf')
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            cur = prefix % p
            remaining = (cur - target) % p
            if remaining in d:
                ans = min(ans, i - d[remaining])
            
            d[cur] = i
        
        return ans if ans != float('inf') and ans != len(nums) else -1