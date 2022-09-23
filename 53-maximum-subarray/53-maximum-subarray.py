class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_so_far = nums[0]
        max_ = nums[0]
        for i in range(1, len(nums)):
            if sum_so_far+nums[i] > nums[i]:
                sum_so_far += nums[i]
            else:
                sum_so_far = nums[i]
            
            max_ = max(max_, sum_so_far)
        
        return max_