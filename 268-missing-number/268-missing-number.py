class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        number = 0
        for num in range(n+1):
            number = number ^ num
        
        for num in nums:
            number = number ^ num
        
        return number