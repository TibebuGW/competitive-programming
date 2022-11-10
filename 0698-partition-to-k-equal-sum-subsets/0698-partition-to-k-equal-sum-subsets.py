class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%k != 0:
            return False
        target = total//k
        available = [True]*n
        memo = {}
        def backtrack(count, current_subset_sum, index, mask):
            if mask in memo:
                return memo[mask]
            if count == k-1:
                memo[mask] = True
                return memo[mask]
            
            if current_subset_sum == target:
                return backtrack(count+1, 0, 0, mask)
            
            for i in range(index, len(nums)):
                if available[i] and current_subset_sum + nums[i] <= target:
                    available[i] = False
                    
                    mask ^= (1<<(n-i))
                    if backtrack(count, current_subset_sum+nums[i], index+1, mask):
                        memo[mask] = True
                        return memo[mask]
                    mask ^= (1<<(n-i))
                    
                    available[i] = True
            
            memo[mask] = False
            return memo[mask]
        
        mask = (1<<n)-1
        return backtrack(0, 0, 0, mask)