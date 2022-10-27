class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[i] != nums[nums[i]-1]:
                # print(nums, i, nums[i], nums[nums[i]])
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
    
        return len(nums)+1