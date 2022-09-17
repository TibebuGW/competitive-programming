class Solution:
        
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum + nums[i] > nums[i]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
                
            max_so_far = max(max_so_far, cur_sum)
            
        return max_so_far