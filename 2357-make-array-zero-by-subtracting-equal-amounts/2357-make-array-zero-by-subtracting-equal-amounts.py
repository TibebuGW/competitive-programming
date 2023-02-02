class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        count = 0
        for i in range(len(nums)):
            nums[i] -= total
            if nums[i]:
                total += nums[i]
                count += 1
                nums[i] = 0
        
        return count