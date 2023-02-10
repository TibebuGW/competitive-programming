class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l = 0
        r = len(nums) - 1
        best = float('inf')
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < 0:
                l = mid + 1
            else:
                best = mid
                r = mid - 1
        
        pos_pointer = best
        neg_pointer = best - 1
        
        if best == float('inf'):
            pos_pointer = len(nums)
            neg_pointer = len(nums) - 1
        elif best == 0:
            neg_pointer = -1
            pos_pointer = 0
            
        while pos_pointer < len(nums) and neg_pointer >= 0:
            if abs(nums[pos_pointer]) < abs(nums[neg_pointer]):
                result.append(nums[pos_pointer] ** 2)
                pos_pointer += 1
            elif abs(nums[pos_pointer]) > abs(nums[neg_pointer]):
                result.append(nums[neg_pointer] ** 2)
                neg_pointer -= 1
            else:
                result.append(nums[neg_pointer] ** 2)
                result.append(nums[pos_pointer] ** 2)
                neg_pointer -= 1
                pos_pointer += 1
        
        while pos_pointer < len(nums):
            result.append(nums[pos_pointer] ** 2)
            pos_pointer += 1
        
        while neg_pointer >= 0:
            result.append(nums[neg_pointer] ** 2)
            neg_pointer -= 1
        
        return result