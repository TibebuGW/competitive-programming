class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[i] != nums[nums[i]-1]:
                # print(nums, i, nums[i], nums[nums[i]])
                cur_index = i
                replaced_index = nums[i]-1
                nums[cur_index], nums[replaced_index] = nums[replaced_index], nums[cur_index] 
                
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
    
        return len(nums)+1