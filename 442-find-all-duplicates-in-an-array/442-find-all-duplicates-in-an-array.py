class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                ans.append(nums[i])
            prev = nums[i]
        
        return ans