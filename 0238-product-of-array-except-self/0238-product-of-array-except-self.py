class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums:
            prefix.append(num * prefix[-1])
        
        suffix = [1]
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(nums[i] * suffix[-1])
        
        suffix = suffix[::-1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i + 1])
        
        return ans