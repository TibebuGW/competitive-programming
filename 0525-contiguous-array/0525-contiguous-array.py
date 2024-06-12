class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        d = {}
        ans = 0
        
        for i in range(len(nums)):
            zeros += int(nums[i] == 0)
            ones += nums[i]
            
            if ones - zeros not in d:
                d[ones - zeros] = i
            
            if ones == zeros:
                ans = max(ans, ones + zeros)
            ans = max(ans, i - d[ones - zeros])
        
        return ans