class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            d[num] += 1
        
        for i in range(len(nums)):
            if 0 <= i <= d[0] - 1:
                nums[i] = 0
            elif d[0] <= i <= d[0] + d[1] - 1:
                nums[i] = 1 
            else:
                nums[i] = 2
        