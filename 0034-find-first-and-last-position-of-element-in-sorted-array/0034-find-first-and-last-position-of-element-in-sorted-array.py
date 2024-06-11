class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flag = False
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                flag = True
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if not flag:
            return [-1, -1]
        
        return [bisect_left(nums, target), bisect_right(nums, target) - 1]