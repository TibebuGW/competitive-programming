# import time
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start = time.time()
        left = 0
        right = len(numbers)-1
        
        while True:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        
        