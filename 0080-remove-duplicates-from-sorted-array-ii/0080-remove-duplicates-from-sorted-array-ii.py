class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0
        runner = 0
        
        while runner < len(nums):
            first_index = runner
            while runner < len(nums) and nums[runner] == nums[first_index]:
                runner += 1
            
            nums[writer] = nums[first_index]
            writer += 1
            if runner - first_index >= 2:
                nums[writer] = nums[first_index]
                writer += 1
        
        return writer