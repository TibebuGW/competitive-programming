class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        walker = 0
        runner = 0
        
        while runner < len(nums):
            if nums[runner] != 0:
                nums[walker] = nums[runner]
                walker += 1
            runner += 1
        
        while walker < len(nums):
            nums[walker] = 0
            walker += 1
        
        