class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counted_once = 0
        counted_twice = 0
        
        for num in nums:
            counted_once = (counted_once ^ num) & ~counted_twice
            counted_twice = (counted_twice ^ num) & ~counted_once
        
        return counted_once