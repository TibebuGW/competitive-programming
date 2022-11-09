class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
            
        for num in range(1, len(nums)+1):
            bitmask ^= num
        
        checker = 1
        while True:
            if bitmask&checker:
                break
            checker <<= 1
        
        division_1 = division_2 = 0
        another_division_1 = another_division_2 = 0
        for num in range(1, len(nums)+1):
            if checker & num:
                division_1 ^= num
            else:
                division_2 ^= num
        
        for num in nums:
            if checker & num:
                another_division_1 ^= num
            else:
                another_division_2 ^= num
        
        num1 = division_1^another_division_1
        num2 = division_2^another_division_2
        for num in nums:
            if num == num2:
                return [num2, num1]
        return [num1, num2]