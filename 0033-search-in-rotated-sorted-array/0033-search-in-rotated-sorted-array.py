class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        min_ = float('inf')
        min_index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < min_:
                min_ = nums[mid]
                min_index = mid
                
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
                
        if min_index == 0:
            if  not (nums[0] <= target <= nums[-1]):
                return -1
            l = 0
            r = len(nums) - 1
        else:
            if not (nums[min_index] <= target <= nums[min_index - 1]):
                return -1
            
            if nums[min_index] <= target <= nums[-1]:
                l = min_index
                r = len(nums) - 1
            else:
                l = 0
                r = min_index - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1