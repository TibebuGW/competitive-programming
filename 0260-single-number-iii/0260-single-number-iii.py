class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        both_numbers = 0
        for num in nums:
            both_numbers ^= num
        
        bit_count = 0
        while both_numbers:
            if both_numbers&1:
                break
            else:
                bit_count += 1
                both_numbers >>= 1
        division_1 = 0
        division_2 = 0
        checker = 1<<bit_count
        for num in nums:
            if num&checker:
                division_1 ^= num
            else:
                division_2 ^= num
        
        return [division_1, division_2]