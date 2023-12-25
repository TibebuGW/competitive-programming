class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        l = 0
        
        while l < len(nums):
            
            r = l
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            
            nums[i] = nums[l]
            l = r
            i += 1
        
        return i