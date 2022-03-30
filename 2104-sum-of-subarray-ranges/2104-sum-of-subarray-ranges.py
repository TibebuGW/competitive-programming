class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums) - 1):
            min_A = max_A = nums[i]

            for j in range(i + 1, len(nums)):
                if nums[j] < min_A:
                    min_A = nums[j]
                if nums[j] > max_A:
                    max_A = nums[j]
                total += max_A - min_A
        return total
                    
                