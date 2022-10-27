class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[i] != nums[nums[i]-1]:
                temp1 = nums[i]
                temp2 = nums[nums[i]-1]
                nums[nums[i]-1] = temp1
                nums[i] = temp2
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1