class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        prefix = 0
        
        
        for i in range(len(nums)):
            prefix += nums[i]
            cur = prefix % k
            if cur in d:
                if i - d[cur] >= 2:
                    return True
            else:
                d[cur] = i
        
        return False