class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                count += 1
                nums[right] = 101
                right += 1
            else:
                left = right
                right += 1
        
        nums.sort()
        return len(nums)-count