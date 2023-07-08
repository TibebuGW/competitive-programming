class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        sum_so_far = float('-inf')
        
        for num in nums:
            if num + sum_so_far < num:
                sum_so_far = num
            else:
                sum_so_far += num
            max_ = max(max_, sum_so_far)
        
        return max_