class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = writer = right = 0
        
        while right < len(nums):
            
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            
            nums[writer] = nums[left]
            left = right
            writer += 1
        
        return writer